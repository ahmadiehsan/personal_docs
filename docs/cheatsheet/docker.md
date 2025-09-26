# Docker

## Image

=== "Remove none"

    ```shell
    docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
    ```

=== "Build"

    ```shell
    docker build . --tag <image_tag>
    ```

=== "Create from container"

    ```shell
    docker commit <container_name>
    docker tag <created_image_id> <image_name:image_tag>
    ```

=== "Login & push to other registry"

    ```shell
    docker login mgit.mparsict.com:5050
    docker build -t mgit.mparsict.com:5050/edx/darsup/mp-media-service:juniper.master .
    docker push mgit.mparsict.com:5050/edx/darsup/mp-media-service:juniper.master
    docker logout mgit.mparsict.com:5050
    ```

## Container

=== "Stop all"

    ```shell
    docker container stop $(docker ps -a -q)
    ```

=== "Remove all"

    ```shell
    docker container rm $(docker ps -a -q)
    ```

=== "Keep alive"

    ```docker
    CMD ["tail", "-f", "/dev/null"]
    ```

=== "Create from image"

    ```shell
    docker run -p 80:80 --name <container_name> -d <image_tag>
    ```

=== "Run command"

    ```shell
    docker exec -it <container_name> <command: bash>
    ```

## Other

- Add current user to Docker group:

    ```shell
    sudo usermod -aG docker $USER
    ```

- Remove all containers log:

    ```shell
    sudo sh -c "truncate -s 0 /var/lib/docker/containers/*/*-json.log"
    ```
