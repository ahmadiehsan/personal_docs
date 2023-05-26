# Git

## Links

- [Git assume a file unchanged](https://stackoverflow.com/a/10881296)

## Commands History

`git reflog`

## Change Default Branch

`git branch --set-upstream-to=origin/<BRANCH NAME>`

tip: with this command you can use `git pull` and `git push` without need to specify a branch name

## Stash

- apply: `git stash apply [stash@{<index>}]`

- list of stashes: `git stash list`

- drop: `git stash drop [stash@{<index>}]`

- clear (drop all stashes): `git stash clear`

- pop (apply and drop): `git stash pop [stash@{<index>}]`

- show (files that changed in this stash): `git stash show [stash@{<index>}]`

## Tag

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

## Ssh

1. generate ssh key: `ssh-keygen -t rsa`
2. add private key to system by: `ssh-add`
3. get public ssh key by this command: `cat ~/.ssh/id_rsa.pub`
4. add public ssh key to git profile setting: [https://github.com/settings/keys](https://github.com/settings/keys)
5. change project remote URL, to ssh type
6. connect to git: `ssh -T git@github.com`

## Token And In Url Auth

- personal access token usage:

  `git clone https://oauth2:<Personal Access Tokens>@gitlab.com/myrepo.git`

  `git clone https://gitlab-ci-token:<Personal Access Tokens>@gitlab.com/myrepo.git`

- simple auth:

  `git clone https://<username>:<password>@gitlab.com/myrepo.git`

- npm packages.json:

  `git+http://<deploy token username>:<projects deploy tocken>@gitlab.com/myrepo.git`

## Alias
`git config --global alias.<command name> "<command>"`

E.X. `git config --global alias.hist "log --all --oneline --graph --decorate"`

## Default Editor

`git config --global core.editor "<editor name: vim>"`

## Password Cache

`git config --global credential.helper 'cache --timeout=<time in seconds: 3600>'`

## Last Pull Time

`stat -c %y .git/FETCH_HEAD`

## Ssl Problem

`git config --global http.sslverify false`

## History Change!

```bash
#!/bin/bash

git filter-branch -f --env-filter '
ea_name="Ehsan Ahmadi"
ea_email="1374ea@gmail.com"

export GIT_AUTHOR_NAME=$ea_name
export GIT_COMMITTER_NAME=$ea_name
export GIT_AUTHOR_EMAIL=$ea_email
export GIT_COMMITTER_EMAIL=$ea_email

cd="$GIT_COMMITTER_DATE"

cd_timestamp=$(echo $cd | cut -d" " -f1 | xargs -IT  date -d T +"%s" )

offset=9331200
compress=1

if test -n "${last_commit_timestamp}"
then
	result=$(( (cd_timestamp - last_cd_timestamp) / $compress ))

	if [ $result -lt 86400 ]
	then
		number=86400
	else
		number=$result
	fi

	commit_timestamp=$(( last_commit_timestamp + number ))
else
	commit_timestamp=$(( $(date -d T +"%s") - $offset ))
fi

export GIT_AUTHOR_DATE="$commit_timestamp"
export GIT_COMMITTER_DATE="$commit_timestamp"

last_cd_timestamp=$cd_timestamp
last_commit_timestamp=$commit_timestamp
'
```
