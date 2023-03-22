import { Duration, Stack, StackProps } from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as kms from 'aws-cdk-lib/aws-kms';
import { Construct } from 'constructs';
import * as fs from 'fs'


export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);


    const s3Bucket = new s3.Bucket(this, 'Bucket-dg-stack-1', {
    bucketName: "cdk-bucket-test-dg",
    versioned: true,
    encryptionKey: new kms.Key(this, 's3BucketKMSKey'),
    lifecycleRules: [
        {
          transitions: [
            {
              storageClass: s3.StorageClass.INFREQUENT_ACCESS,
              transitionAfter: Duration.days(30),
            },
            {
              storageClass: s3.StorageClass.GLACIER,
              transitionAfter: Duration.days(90),
            },
          ],
        },
      ],
    });

 const S3Access = new iam.PolicyDocument({
      statements: [
        new iam.PolicyStatement({
          resources: ['arn:aws:s3:::*'],
          actions: ['s3:*'],
        }),
      ],
    });


    const role = new iam.Role(this, 'example-iam-role', {
      assumedBy: new iam.ServicePrincipal('ec2.amazonaws.com'),
      description: 'An example IAM role in AWS CDK',
      inlinePolicies: {
        S3Access: S3Access,
      },
      
    });

    const vpc = ec2.Vpc.fromLookup(this, 'DefaultVpc', {isDefault: true });

    const securityGroup = new ec2.SecurityGroup(this,'cdk-ec2-sg',{
        vpc: vpc,
        allowAllOutbound: true, 
        securityGroupName: 'cdk-instance-sg',
      }
    )
    securityGroup.addIngressRule(
         ec2.Peer.anyIpv4(),
         ec2.Port.tcp(22),
         'Allows SSH access from Internet'
    )
    securityGroup.addIngressRule(
      ec2.Peer.anyIpv4(),
      ec2.Port.tcp(80),
      'Allows HTTP access from Internet'
    )
    const instance = new ec2.Instance(this, 'simple-instance-1', {
      vpc: vpc,
      securityGroup: securityGroup,
      instanceName: 'cdk-instance',
      role: role,
      instanceType: ec2.InstanceType.of(
        ec2.InstanceClass.T2,
        ec2.InstanceSize.MICRO
      ),
      machineImage: ec2.MachineImage.latestAmazonLinux({
        generation: ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
      }),

      keyName: 'DG',
    })
 
   instance.addUserData(
      fs.readFileSync('lib/user_script.sh', 'utf8')
    )


  }
}
