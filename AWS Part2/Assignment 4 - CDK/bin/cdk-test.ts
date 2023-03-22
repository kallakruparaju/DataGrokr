import * as cdk from 'aws-cdk-lib';
import { CdkTestStack } from '../lib/cdk-test-stack';

const app = new cdk.App();
new CdkTestStack(app, 'CdkTestStack', {
  env: {
    account: '628906266361',
    region: 'ap-south-1'
  }
});