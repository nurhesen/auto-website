#!/bin/bash

sudo yum update -y
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -a -G docker $(whoami)
sudo usermod -aG docker $USER
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose


sudo docker-compose build
sudo docker-compose up react


# Specify the file path and name
nginx_config_file="docker-compose-app.service"
current_location="$(pwd)"


# Nginx configuration content with user-provided IP
nginx_config="
[Unit]
Description=Docker Compose Application
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=true
ExecStart=/usr/local/bin/docker-compose -f $current_location/docker-compose.yml up --scale react=0
ExecStop=/usr/local/bin/docker-compose -f $current_location/docker-compose.yml down

[Install]
WantedBy=default.target
"

# Write the configuration to the file (replace the existing file)
echo "$nginx_config" | sudo tee "$nginx_config_file" > $nginx_config_file

# Optionally, display a message indicating success
echo "Nginx configuration file created successfully at: $nginx_config_file"


sudo cp -f docker-compose-app.service /etc/systemd/system/
sudo rm docker-compose-app.service
sudo systemctl daemon-reload
sudo systemctl enable docker-compose-app
sudo systemctl start --no-block docker-compose-app


sudo reboot
