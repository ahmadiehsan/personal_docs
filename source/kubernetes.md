# Kubernetes

## generate clean secret

```
echo "PASSWORD" | tr -d \\n | base64 -w 0
```

