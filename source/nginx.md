# Nginx

## run nginx on startup
`sudo update-rc.d nginx enable`

## test
`sudo nginx -t`

## simple config

```
server {
    listen 443 ssl;
    server_name video.darsup.org;
    location / {
        include proxy_params;
        proxy_pass http://localhost:8002;
    }
}

server {
    if ($host = marketing.darsup.org) {
        return 301 https://$host$request_uri;
    }

    listen 80;
    server_name marketing.darsup.org;
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

