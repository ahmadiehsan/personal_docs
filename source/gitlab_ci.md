# GitLab CI

## install gitlab-runner on server

Follow [installation guide](https://docs.gitlab.com/runner/install/#containers)

## create system service

`sudo gitlab-runner install --working-directory /home/<unix_user> --user <unix_user>`

`sudo service gitlab-runner <status|start|stop|restart>`

## create new runner

`sudo gitlab-runner register`

## get list of runners

`sudo gitlab-runner verify`

## delete removed runners

`sudo gitlab-runner verify --delete`

