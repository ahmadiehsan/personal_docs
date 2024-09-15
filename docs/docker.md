# Docker

## Links

- [Check For Docker Proper Installation On The Production Server](https://github.com/docker/docker-bench-security)
- [Multiple Databases With The Official Postgresql Docker Image](https://github.com/mrts/docker-postgresql-multiple-databases)

## Image

- Remove none images:

  ```
  docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
  ```

- Build image:

  ```
  docker build . --tag <image_tag>
  ```

- Create image from container:

  ```
  docker commit <container_name>
  docker tag <created_image_id> <image_name:image_tag>
  ```

- Login & push to other registry:

  ```
  docker login mgit.mparsict.com:5050
  docker build -t mgit.mparsict.com:5050/edx/darsup/mp-media-service:juniper.master .
  docker push mgit.mparsict.com:5050/edx/darsup/mp-media-service:juniper.master
  docker logout mgit.mparsict.com:5050
  ```

## Container

- Stop all containers:

  ```
  docker container stop $(docker ps -a -q)
  ```

- Remove all containers:

  ```
  docker container rm $(docker ps -a -q)
  ```

- Keep container alive:

  ```
  CMD ["tail", "-f", "/dev/null"]
  ```

- Create container from image:

  ```
  docker run -p 80:80 --name <container_name> -d <image_tag>
  ```

- Run command in container:

  ```
  docker exec -it <container_name> <command: bash>
  ```

## Other

- Add current user to Docker group:

  ```
  sudo usermod -aG docker $USER
  ```

- Remove all containers log:

  ```
  sudo sh -c "truncate -s 0 /var/lib/docker/containers/*/*-json.log"
  ```
