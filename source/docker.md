# Docker

## remove none images

```
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
```

## stop/remove all containers

```
docker container stop $(docker ps -a -q)
docker container rm $(docker ps -a -q)
```

