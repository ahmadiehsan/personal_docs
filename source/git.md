# Git

## Links

- [Git assume a file unchanged](https://stackoverflow.com/a/10881296)
- [Delete a Git branch locally and remotely](https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-locally-and-remotely/2003515#2003515)

## Reflog

1. See logs:

   ```
   git reflog
   ```
2. Undo an action:

   ```
   git reset --hard <reflog_id: HEAD@{2}>
   ```

## Stash

- Apply: 

  ```
  git stash apply stash@{<index>}
  ```

- List of stashes:

  ```
  git stash list
  ```

- Drop:

  ```
  git stash drop stash@{<index>}
  ```

- Clear (drop all stashes):

  ```
  git stash clear
  ```

- Pop (apply and drop):

  ```
  git stash pop stash@{<index>}
  ```

- Show (files that changed in this stash):

  ```
  git stash show stash@{<index>}
  ```

## Tag

- Create:
  
  ```
  # Without message
  git tag <tag_name>
  
  # with message
  git tag <tag_name> -m "<message>"
  
  # Add tag to specific commit
  git tag <tag_name> <commit_id>
  ```
  
- Update:

  ```
  # Without message
  git tag -f <tag_name> <commit_id>
  
  # with message
  git tag -f <tag_name> -m "<message>"
  ```

- List of tags:

  ```
  # Simple
  git tag
  
  # More verbose
  git tag --list
  ```

- Delete:
  
  ```
  # For local repo
  git tag --delete <tag_name>
  
  # For remote repo
  git push origin --delete <tag_name>
  ```
  
- Tag data:

  ```
  git show <tag_name>
  ```

- Push tags:
  
  ```
  # Single tag
  git push origin <tag_name>
  
  # All tags
  git push origin master --tags
  ```

## Auth (SSH)

1. Generate ssh key:

   ```
   ssh-keygen -t rsa
   ```
2. Add private key to system by:

   ```
   ssh-add
   ```
3. Get public ssh key by this command:

   ```
   cat ~/.ssh/id_rsa.pub
   ```
4. Add public ssh key to git profile setting:

   [https://github.com/settings/keys](https://github.com/settings/keys)
5. Change project remote URL, to ssh type
6. Connect to git:

   ```
   ssh -T git@github.com
   ```

## Auth (Token & In-URL Auth)

- Personal access token:

  ```
  # With OAuth2
  git clone https://oauth2:<access_token>@gitlab.com/myrepo.git
  
  # With username
  git clone https://<username>:<access_token>@gitlab.com/myrepo.git
  ```

- Simple auth:

  ```
  git clone https://<username>:<password>@gitlab.com/myrepo.git
  ```

- PIP:

  ```
  git+https://<username>:<access_token>@gitlab.com/myrepo.git@<tag>
  ```

- NPM:

  ```
  git+https://<username>:<access_token>@gitlab.com/myrepo.git
  ```


## Alias

- Add:

  ```
  git config --global alias.<command_name> "<command>"
  
  # Example
  git config --global alias.hist "log --all --oneline --graph --decorate"
  ```

## Config

- Default editor:

  ```
  git config --global core.editor "<editor name: vim>"
  ```
- Password cache:

  ```
  git config --global credential.helper 'cache --timeout=<time in seconds: 3600>'
  ```
- SSL problem:

  ```
  git config --global http.sslverify false
  ```

## Pull/Push

- Last pull time:

  ```
  stat -c %y .git/FETCH_HEAD
  ```
