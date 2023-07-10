# Gitlab Ci

## Links

- [Change Gitlab runner user](https://stackoverflow.com/questions/37187899/change-gitlab-ci-runner-user/40703269#40703269)
- [Gitlab runner: job failed preparing environment](https://stackoverflow.com/questions/63154881/the-runner-of-type-shell-dont-work-job-failed-system-failure-preparing-envi/66285094#66285094)

## Install Gitlab-Runner On Server

Follow [installation guide](https://docs.gitlab.com/runner/install/#containers)

## Create System Service

`sudo gitlab-runner install --working-directory /home/<unix_user> --user <unix_user>`

`sudo service gitlab-runner <status|start|stop|restart>`

## Create New Runner

`sudo gitlab-runner register`

## Get List Of Runners

`sudo gitlab-runner verify`

## Delete Removed Runners

`sudo gitlab-runner verify --delete`

