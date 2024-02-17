#!/bin/bash

# Check if argument exists
if [ -z $1 ]; then
    server_ip = "$1"
else
    # If there is no argument then prompt user for the server IP address
    read -p "Enter the domain or server IP address: " server_ip
fi
# Specify the file path and name
nginx_config_file="deploy-commands/iberry"
current_location="$(pwd)"

# Nginx configuration content with user-provided IP
nginx_config="
server {
    listen 80;
    server_name $server_ip;

    location / {
        alias $current_location/react-app/build/;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;

    }

    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    }

    location /admin {
        proxy_pass http://localhost:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    }

    location /dj-static/ {
        alias $current_location/out/;
    }

    location /media/ {
        alias $current_location/media/;
    }
}
"

# Write the configuration to the file (replace the existing file)
echo "$nginx_config" | sudo tee "$nginx_config_file" > /dev/null

# Optionally, display a message indicating success
echo "Nginx configuration file created successfully at: $nginx_config_file"
