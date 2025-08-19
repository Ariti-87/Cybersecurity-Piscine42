# Tor Hidden Web Server

## 📝 Project Overview
This project aims to create a static web server accessible via the **Tor network** using a hidden service. The server hosts a single web page (`index.html`) and is configured with **Nginx**. Access to the server is available over HTTP on port 80 and via SSH on port 4242.

## 💻 Setup & Installation

### 1. System Setup
Update packages and install required software:
```bash
sudo apt update
sudo apt install nginx tor openssh-server
```

### 2. Static Web Page
Create the HTML file to serve:
```bash
sudo nano /var/www/html/index.html
```

Example content:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello Tor</title>
</head>
<body>
    <h1>Dealer de Meth</h1>
    <p>Site en construction, plein de nouveau produit en stock, préparez la CB</p>
</body>
</html>
```

### 3. Nginx Configuration
Edit the Nginx configuration:
```bash
sudo nano /etc/nginx/sites-available/default
```

Ensure the following configuration:
```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html;
    server_name localhost;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

Test and reload Nginx:
```bash
sudo nginx -t
sudo systemctl reload nginx
```

### 4. SSH Configuration
Edit SSH configuration to use port 4242:
```bash
sudo nano /etc/ssh/sshd_config
```

Set:
```
Port 4242
```

Restart SSH:
```bash
sudo systemctl restart ssh
```

### 5. Tor Hidden Service Configuration
Edit the Tor configuration:
```bash
sudo nano /etc/tor/torrc
```

Add:
```
HiddenServiceDir /var/lib/tor/hidden_service/
HiddenServicePort 80 127.0.0.1:80
```

Restart Tor:
```bash
sudo systemctl restart tor
```

Retrieve your `.onion` address:
```bash
sudo cat /var/lib/tor/hidden_service/hostname
```

---

## 🧪 Testing
- Open the Tor Browser.
- Visit your `.onion` address to see your static page.
- SSH into the server on port 4242 for administrative access.

---

## ⚠️ Notes
- No additional ports or firewall rules should be configured.
- Only **Nginx** is allowed as the web server.
- The project demonstrates understanding of hidden services and basic Tor network setup.

