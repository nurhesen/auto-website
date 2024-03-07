#!/bin/bash

exec >> /var/log/user_data.log 2>&1

# Install Git
yum update -y
yum install git -y

# Set the directory where you want to clone the repository
clone_directory="/home/ec2-user/auto-website"

# Ensure the directory exists
mkdir -p "$clone_directory"

# Clone the public repository
git clone https://github.com/nurhesen/auto-website.git "$clone_directory"
cd "$clone_directory"
git checkout deploy-test


# Get the instance's public IPv4 address
instance_ip=$(curl -s https://checkip.amazonaws.com/)

# Echo the IP address
echo "Instance IP address: $instance_ip"

# Replace "server_ip" in nginx.conf
sed -i "s/auto.nurhesen.click/$instance_ip auto.nurhesen.click/g" /home/ec2-user/auto-website/nginx/nginx.conf

chown -R ec2-user:ec2-user /home/ec2-user

. deploy.sh