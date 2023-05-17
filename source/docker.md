# Docker

## Links

- [Docker Prune](https://stackoverflow.com/questions/46672001/is-it-safe-to-clean-docker-overlay2/46672068#46672068)
- [Check For Docker Proper Install On The Production Server](https://github.com/docker/docker-bench-security)
- [Multiple Databases With The Official Postgresql Docker Image](https://github.com/mrts/docker-postgresql-multiple-databases)

## Remove None Images

```bash
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
```

## Stop/Remove All Containers

```bash
docker container stop $(docker ps -a -q)
docker container rm $(docker ps -a -q)
```

## Add User To Docker Group

```bash
sudo usermod -aG docker $USER
```

## Remove All Containers Log

```bash
sudo sh -c "truncate -s 0 /var/lib/docker/containers/*/*-json.log"
```

## Keep Container Alive

```
CMD ["tail", "-f", "/dev/null"]
```

## Build Image

```bash
docker build . --tag <image_tag>
```

## Create Container From Image

```bash
docker run -p 80:80 --name <container_name> -d <image_tag>
```

## Create Image From Container

```
docker commit <container_name>
docker tag <created_image_id> <image_name:image_tag>
```

## Run Command In Container

```bash
docker exec -it <container_name> bash
```

## Login And Push To Other Registry

```
docker login mgit.mparsict.com:5050
docker build -t mgit.mparsict.com:5050/edx/darsup/mp-media-service:juniper.master .
docker push mgit.mparsict.com:5050/edx/darsup/mp-media-service:juniper.master
docker logout mgit.mparsict.com:5050
```