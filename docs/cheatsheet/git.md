# Git

## Links

- [Git assume a file unchanged](https://stackoverflow.com/a/10881296)
- [Delete a Git branch locally and remotely](https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-locally-and-remotely/2003515#2003515)
- [GitFlow cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/)

## Reflog

1. See logs:

  ```shell
  git reflog
  ```

2. Undo an action:

  ```shell
  git reset --hard <reflog_id: HEAD@{2}>
  ```

## Stash

- Apply:

  ```shell
  git stash apply stash@{<index>}
  ```

- List of stashes:

  ```shell
  git stash list
  ```

- Drop:

  ```shell
  git stash drop stash@{<index>}
  ```

- Clear (drop all stashes):

  ```shell
  git stash clear
  ```

- Pop (apply and drop):

  ```shell
  git stash pop stash@{<index>}
  ```

- Show (files that changed in this stash):

  ```shell
  git stash show stash@{<index>}
  ```

## Tag

- Create:

  ```shell
  # Without message
  git tag <tag_name>

  # with message
  git tag <tag_name> -m "<message>"

  # Add tag to specific commit
  git tag <tag_name> <commit_id>
  ```

- Update:

  ```shell
  # Without message
  git tag -f <tag_name> <commit_id>

  # with message
  git tag -f <tag_name> -m "<message>"
  ```

- List of tags:

  ```shell
  # Simple
  git tag

  # More verbose
  git tag --list
  ```

- Delete:

  ```shell
  # For local repo
  git tag --delete <tag_name>

  # For remote repo
  git push origin --delete <tag_name>
  ```

- Tag data:

  ```shell
  git show <tag_name>
  ```

- Push tags:

  ```shell
  # Single tag
  git push origin <tag_name>

  # All tags
  git push origin master --tags
  ```

## Auth (SSH)

1. Generate ssh key:

  ```shell
  ssh-keygen -t rsa
  ```

2. Add private key to system by:

  ```shell
  ssh-add
  ```

3. Get public ssh key by this command:

  ```shell
  cat ~/.ssh/id_rsa.pub
  ```

4. Add public ssh key to git profile setting: [https://github.com/settings/keys](https://github.com/settings/keys)
5. Change project remote URL, to ssh type
6. Connect to git:

  ```shell
  ssh -T git@github.com
  ```

## Auth (Token & In-URL Auth)

- Personal access token:

  ```shell
  # With OAuth2
  git clone https://oauth2:<access_token>@gitlab.com/myrepo.git

  # With username
  git clone https://<username>:<access_token>@gitlab.com/myrepo.git
  ```

- Simple auth:

  ```shell
  git clone https://<username>:<password>@gitlab.com/myrepo.git
  ```

- PIP:

  ```text
  git+https://<username>:<access_token>@gitlab.com/myrepo.git@<tag>
  ```

- NPM:

  ```text
  git+https://<username>:<access_token>@gitlab.com/myrepo.git
  ```

## Alias

- Add:

  ```shell
  git config --global alias.<command_name> "<command>"

  # Example
  git config --global alias.hist "log --all --oneline --graph --decorate"
  ```

## Config

- Default editor:

  ```shell
  git config --global core.editor "<editor name: vim>"
  ```

- Password cache:

  ```shell
  git config --global credential.helper 'cache --timeout=<time in seconds: 3600>'
  ```

- SSL problem:

  ```shell
  git config --global http.sslverify false
  ```

## Pull/Push

- Last pull time:

  ```shell
  stat -c %y .git/FETCH_HEAD
  ```
