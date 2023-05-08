# Nginx

## Links

- [Leverage Browser Caching](https://stackoverflow.com/questions/20147587/how-to-leverage-browser-caching-in-django#answer-20147630)
- [Minimal Standard Proxy_Pass](https://serverfault.com/questions/112795/how-to-run-a-server-on-port-80-as-a-normal-user-on-linux#answer-450513)
- [Request Entity Too Large](https://www.cyberciti.biz/faq/linux-unix-bsd-nginx-413-request-entity-too-large/)
- [Log Variables](https://serverfault.com/questions/404626/how-to-output-variable-in-nginx-log-for-debugging/580739#580739)
- [Https://Certbot.Eff.Org/Instructions?Ws=Nginx&Amp;Os=Debianbuster](https://certbot.eff.org/instructions?ws=nginx&os=debianbuster)

## Run Nginx On Startup

`sudo update-rc.d nginx enable`

## Test
`sudo nginx -t`

## Simple Config

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

## Ssl Config

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

## Gzip

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

