# Git

## commands history

`git reflog`

## change default branch

`git branch --set-upstream-to=origin/<BRANCH NAME>`

tip: with this command you can use `git pull` and `git push` without need to specify a branch name

## stash

- apply: `git stash apply [stash@{<index>}]`

- list of stashes: `git stash list`

- drop: `git stash drop [stash@{<index>}]`

- clear (drop all stashes): `git stash clear`

- pop (apply and drop): `git stash pop [stash@{<index>}]`

- show (files that changed in this stash): `git stash show [stash@{<index>}]`

## tag

- create:
  - unannotated tag, without message: `git tag <tag name>`
  - annotated tag, with message: `git tag <tag name> -m "message"`
  - add tag to specific commit `git tag <tag name> <commit id>`

- update:

  `git tag -f <tag name> <commit id>`

  `git tag -f <tag name> -m "message"`

- list of tags:

  `git tag`

  `git tag --list`

- delete:
  - for local repo: `git tag --delete <tag name>`
  - for remote repo `git push origin :<tag name>`

- tag data: `git show <tag name>`

- push tags
  - single tag: `git push origin <tag name>`
  - all tags: `git push origin master --tags`

## ssh

1. generate ssh key: `ssh-keygen -t rsa`
2. add private key to system by: `ssh-add`
3. get public ssh key by this command: `cat ~/.ssh/id_rsa.pub`
4. add public ssh key to git profile setting: [https://github.com/settings/keys](https://github.com/settings/keys)
5. change project remote URL, to ssh type
6. connect to git: `ssh -T git@github.com`

## token and in url auth

- personal access token usage:

  `git clone https://oauth2:<Personal Access Tokens>@gitlab.com/myrepo.git`

  `git clone https://gitlab-ci-token:<Personal Access Tokens>@gitlab.com/myrepo.git`

- simple auth:

  `git clone https://<username>:<password>@gitlab.com/myrepo.git`

- npm packages.json:

  `git+http://<deploy token username>:<projects deploy tocken>@gitlab.com/myrepo.git`

## alias
`git config --global alias.<command name> "<command>"`

E.X. `git config --global alias.hist "log --all --oneline --graph --decorate"`

## default editor

`git config --global core.editor "<editor name: vim>"`

## password cache

`git config --global credential.helper 'cache --timeout=<time in seconds: 3600>'`

## last pull time

`stat -c %y .git/FETCH_HEAD`

## ssl problem

`git config --global http.sslverify false`
