#!/bin/bash

sudo su
yum update -y
sudo amazon-linux-extras install nginx1 -y
systemctl start nginx
systemctl enable nginx