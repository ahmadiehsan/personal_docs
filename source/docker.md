# Docker

## remove none images

```bash
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
```

## stop/remove all containers

```bash
docker container stop $(docker ps -a -q)
docker container rm $(docker ps -a -q)
```

## add user to docker group

```bash
sudo usermod -aG docker your-user
```

## remove all containers log

```bash
sudo sh -c "truncate -s 0 /var/lib/docker/containers/*/*-json.log"
```

