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
sudo usermod -aG docker $USER
```

## remove all containers log

```bash
sudo sh -c "truncate -s 0 /var/lib/docker/containers/*/*-json.log"
```

## keep container alive

```
CMD ["tail", "-f", "/dev/null"]
```

## build image

```bash
docker build . --tag <image_tag>
```

## create container from image

```bash
docker run -p 80:80 --name <container_name> -d <image_tag>
```

## create image from container

```
docker commit <container_name>
docker tag <created_image_id> <image_name:image_tag>
```

## run command in container

```bash
docker exec -it <container_name> bash
```

## login and push to other registry

```
docker login mgit.mparsict.com:5050
docker build -t mgit.mparsict.com:5050/edx/darsup/mp-media-service:juniper.master .
docker push mgit.mparsict.com:5050/edx/darsup/mp-media-service:juniper.master
docker logout mgit.mparsict.com:5050
```