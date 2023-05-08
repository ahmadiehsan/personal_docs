# Gitlab Ci

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

