#!/usr/bin/env bash
# Prepare your web server

# install Nginx if not already exists
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file for testing
html_content="<html>
	<head>
		<title>Test Page</title>
	</head>
	<body>
		Test Contnet
	</body>
	</html>"
echo "$html_content" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolc link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ folder
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
nginx_alias="location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n"
sudo sed -i "/server_name _;/a $nginx_alias" "$nginx_config"

# Restart Nginx to apply changes
sudo service nginx restart

exit 0
