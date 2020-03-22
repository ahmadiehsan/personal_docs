# Nginx

## run nginx on startup
`sudo update-rc.d nginx enable`

## test
`sudo nginx -t`

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

