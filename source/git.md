# Git

## Links

- [Git assume a file unchanged](https://stackoverflow.com/a/10881296)
- [Delete a Git branch locally and remotely](https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-locally-and-remotely/2003515#2003515)

## Reflog

1. See logs: `git reflog`
2. Undo an action: `git reset --hard <reflog_id: HEAD@{2}>`

## Stash

- apply: `git stash apply stash@{<index>}`

- list of stashes: `git stash list`

- drop: `git stash drop stash@{<index>}`

- clear (drop all stashes): `git stash clear`

- pop (apply and drop): `git stash pop stash@{<index>}`

- show (files that changed in this stash): `git stash show stash@{<index>}`

## Tag

- create:
  
  - without message: `git tag <tag_name>`
  - with message: `git tag <tag_name> -m "<message>"`
  - add tag to specific commit `git tag <tag_name> <commit_id>`
  
- update:

  `git tag -f <tag_name> <commit_id>`

  `git tag -f <tag_name> -m "<message>"`

- list of tags:

  `git tag`

  `git tag --list`

- delete:
  - for local repo: `git tag --delete <tag_name>`
  - for remote repo `git push origin --delete <tag_name>`

- tag data: `git show <tag_name>`

- push tags:
  - single tag: `git push origin <tag_name>`
  - all tags: `git push origin master --tags`

## Auth

- ssh:

  1. generate ssh key: `ssh-keygen -t rsa`
  2. add private key to system by: `ssh-add`
  3. get public ssh key by this command: `cat ~/.ssh/id_rsa.pub`
  4. add public ssh key to git profile setting: [https://github.com/settings/keys](https://github.com/settings/keys)
  5. change project remote URL, to ssh type
  6. connect to git: `ssh -T git@github.com`

- token & in url auth:

  - personal access token:

    `git clone https://oauth2:<access_token>@gitlab.com/myrepo.git`

    `git clone https://<username>:<access_token>@gitlab.com/myrepo.git`

  - simple auth: `git clone https://<username>:<password>@gitlab.com/myrepo.git`

  - pip: `git+https://<username>:<access_token>@gitlab.com/myrepo.git@<tag>`

  - npm: `git+https://<username>:<access_token>@gitlab.com/myrepo.git`


## Alias

- add: `git config --global alias.<command_name> "<command>"`
- example: `git config --global alias.hist "log --all --oneline --graph --decorate"`

## Config

- default editor: `git config --global core.editor "<editor name: vim>"`
- password cache: `git config --global credential.helper 'cache --timeout=<time in seconds: 3600>'`
- ssl problem: `git config --global http.sslverify false`

## Pull/Push

- last pull time: `stat -c %y .git/FETCH_HEAD`
