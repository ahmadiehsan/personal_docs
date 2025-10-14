# CI/CD

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
          - make dependencies.install
          - make manage.build
    ```
