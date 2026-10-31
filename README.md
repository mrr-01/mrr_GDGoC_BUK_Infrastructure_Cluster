# CampusBoard v1

A static web page serving central campus events and announcements.

## Local Setup Instructions

### Prerequisites
- Linux system with NGINX installed

### Serving with NGINX
1. Place or link project contents into your web root or custom directory:
   `sudo mkdir -p /var/www/campusboard`

   `/var/www/campusboard`

2. Configure NGINX (`/etc/nginx/conf.d/campusboard.conf`):
   ```nginx
   server {
       listen 8080;
       server_name localhost;

       location / {
           root /home/mrr_fedora/mrr/infra/week2/campusboard;
           index index.html;
       }
   }
    ```

3. Test and reload NGINX
  ```bash
  sudo nginx -t && sudo systemctl reload nginx```
