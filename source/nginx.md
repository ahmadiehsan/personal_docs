# Nginx

## run nginx on startup
`sudo update-rc.d nginx enable`

## test
`sudo nginx -t`

## simple config

```
server {
    listen 80;
    server_name video.darsup.org;
    location / {
        include proxy_params;
        proxy_pass http://localhost:8002;
    }
}
```

## ssl config

```
server {
    server_name video.darsup.org;
    location / {
        include proxy_params;
        proxy_pass http://localhost:8002;
    }

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/marketing.darsup.org/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/marketing.darsup.org/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}

server {
    if ($host = video.darsup.org) {
        return 301 https://$host$request_uri;
    }

    listen 80;
    server_name video.darsup.org;
    return 404;
}
```

## gzip

```
server {
	gzip on;
    gzip_proxied any;
    gzip_types
        text/css
        text/javascript
        text/xml
        text/plain
        application/javascript
        application/x-javascript
        application/json;
}
```

