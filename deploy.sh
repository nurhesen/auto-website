#!/bin/bash
cd "$(dirname "$0")"


echo "Overwriting nginx configuration"
sh deploy-commands/overwrite-nginx-config.sh $1


sleep 2

echo "Overwriting systemd configuration"
sh deploy-commands/overwrite-systemd-config.sh

sleep 2

echo "Installing Docker"
sh deploy-commands/install-docker.sh

sleep 2

echo "Installing Docker compose"
sh deploy-commands/install-docker-compose.sh

sleep 2

echo "Setting Docker permissions"
sh deploy-commands/docker-permission.sh

sleep 10

echo "Building docker container"
sudo docker-compose build &

# Capture the process ID of the last background command
build_pid=$!

# Wait for the build process to finish
wait $build_pid

# Continue with the rest of your script after the build is complete
echo "Docker-compose build has finished, continuing with the script."

sleep 2

echo "Setting up systemctl"
sh deploy-commands/setup-systemctl.sh

sleep 2

echo "Setting up nginx"
sh deploy-commands/setup-nginx.sh


# Delete scripts
rm -r "deploy-commands"
rm "$0"

echo "Rebooting..."
sudo reboot