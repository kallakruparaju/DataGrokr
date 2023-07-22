FROM centos:7
RUN yum install java-11-openjdk -y
RUN yum install git -y
RUN yum install openssh-server -y
RUN ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa
RUN ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N '' -t rsa
RUN ssh-keygen -t ed25519 -f ssh_host_ed25519_key -N '' -t rsa
RUN yum install python wget unzip curl -y
RUN wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
RUN unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
RUN ./sam-installation/install
RUN yum install awscli -y
RUN rm -rf aws-sam-cli-linux-x86_64.zip
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]