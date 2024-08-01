# Docker

## Links

- [Check For Docker Proper Installation On The Production Server](https://github.com/docker/docker-bench-security)
- [Multiple Databases With The Official Postgresql Docker Image](https://github.com/mrts/docker-postgresql-multiple-databases)

## Image

- remove none images: `docker rmi $(docker images --filter "dangling=true" -q --no-trunc)`

- build image: `docker build . --tag <image_tag>`

- create image from container:

  ```
  docker commit <container_name>
  docker tag <created_image_id> <image_name:image_tag>
  ```

- login & push to other registry:

  ```
  docker login mgit.mparsict.com:5050
  docker build -t mgit.mparsict.com:5050/edx/darsup/mp-media-service:juniper.master .
  docker push mgit.mparsict.com:5050/edx/darsup/mp-media-service:juniper.master
  docker logout mgit.mparsict.com:5050
  ```

## Container

- stop all containers: `docker container stop $(docker ps -a -q)`
- remove all containers: `docker container rm $(docker ps -a -q)`
- keep container alive: `CMD ["tail", "-f", "/dev/null"]`
- create container from image: `docker run -p 80:80 --name <container_name> -d <image_tag>`
- run command in container: `docker exec -it <container_name> <command: bash>`

## Log

- remove all containers log: `sudo sh -c "truncate -s 0 /var/lib/docker/containers/*/*-json.log"`

## Docker Group

- add the current user: `sudo usermod -aG docker $USER`