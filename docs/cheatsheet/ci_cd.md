# CI/CD

## Links

- [Change Gitlab runner user](https://stackoverflow.com/questions/37187899/change-gitlab-ci-runner-user/40703269#40703269)
- [Gitlab runner: job failed preparing environment](https://stackoverflow.com/questions/63154881/the-runner-of-type-shell-dont-work-job-failed-system-failure-preparing-envi/66285094#66285094)

## GitLab CI

- Install Gitlab-Runner on server: [installation guide](https://docs.gitlab.com/runner/install/#containers)
- Create system service:

  ```shell
  sudo gitlab-runner install --working-directory /home/<unix_user> --user <unix_user>
  sudo service gitlab-runner <status|start|stop|restart>
  ```

- Create new runner:

  ```shell
  sudo gitlab-runner register
  ```

- List of runners:

  ```shell
  sudo gitlab-runner verify
  ```

- Delete removed runners:

  ```shell
  sudo gitlab-runner verify --delete
  ```

- Sample `.gitlab-ci.yml` file:

  ```yaml
  stages:
    - deploy

  variables:
    PROJECT_DIR: "/ahmadiehsan/app/personal_docs"
    PROJECT_ENV_DIR: "/ahmadiehsan/app/env_personal_docs"

  deploy:
    stage: deploy
    rules:
      - if: '$CI_COMMIT_BRANCH == "master"'
    variables:
      GIT_STRATEGY: none
    script:
      - cd $PROJECT_DIR
      - git remote set-url origin $CI_REPOSITORY_URL
      - git reset --hard
      - git checkout $CI_COMMIT_BRANCH
      - git fetch -p origin $CI_COMMIT_BRANCH
      - git reset --hard origin/$CI_COMMIT_BRANCH
      - source $PROJECT_ENV_DIR/bin/activate
      - make requirements.install
      - make manage.build
  ```
