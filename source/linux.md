# Linux

## disk space

`df -h`

## ssh

- download to local:

  `scp -[r]P <port> <user>@<ip>:<path/to/folder> <path/to/local>`

- upload to server:

  `scp -[r]P <port> <source file> <username>@<destination server>:<destination directory>`

- generate ssh key:

  ```
  ssh-keygen -t rsa
  ssh-add
  ```

- list of private keys: `ssh-add -l`

- you can access to you public ssh key by this command: `cat ~/.ssh/id_rsa.pub`

- prevent SSH from disconnecting:

  ```shell
  # /etc/ssh/ssh_config or ~/.ssh/config
  
  ServerAliveInterval 60
  ```

## Contrib / non-free repo

```
# /etc/apt/sources.list

deb http://deb.debian.org/debian/ buster main contrib non-free
deb-src http://deb.debian.org/debian/ buster main contrib non-free

deb http://security.debian.org/debian-security buster/updates main contrib non-free
deb-src http://security.debian.org/debian-security buster/updates main contrib non-free

deb http://deb.debian.org/debian/ buster-updates main contrib non-free
deb-src http://deb.debian.org/debian/ buster-updates main contrib non-free
```

## Compress and Extract

```shell
# compress (tar)
tar -czvf <name-of-archive.tgz> </path/to/directory>
tar -czvf <name-of-archive.tgz> </path/to/directory>/.	# include hidden files
tar -czvf <name-of-archive.tgz> </path/to/file>

# extract (tar)
tar -xzvf <name-of-archive.tgz>
tar -xzvf <name-of-archive.tgz> -C </path/to/directory>

# extract (tar)  # sudo apt-get install unrar
unrar x -r </path/to/file.rar>
```

## Cron

1. add file without ".sh" to `/etc/cron.daily/`
2. or add corn command to `/etc/crontab`
3. test for correct run: `run-parts --test /etc/cron.daily`

## Firewall

- enable and disable firewall: `sudo ufw enable/disable`

- get status of firewall and all available ports: `sudo ufw status verbose`

- get list of apps that wanna firewall access: `sudo ufw app list`

- set or get firewall access for app:

  `sudo ufw allow <port>`
  
  `sudo ufw delete allow <port>`
  
  `sudo ufw allow in "<app name>"`
  
  `sudo ufw delete allow in "<app name>"`

## Add proxy to apt-get

1. go to https://free-proxy-list.net/ and find an free proxy address

2. add below code to `/etc/apt/apt.conf`

   - if your proxy has not password

     `Acquire::http::Proxy "http://<yourproxyaddress>:<proxyport>";`

   - if your proxy has password

     `Acquire::http::Proxy "http://<username>:<password>@<proxyaddress>:<proxyport>";`

## remove launcher entry

1. go to
   - `~/.local/share/applications/` if you create entry for you user only
   - `/usr/share/applications/` if you create entry for all users
2. remove `<your application name: jetbrains-pycharm.desktop>`

## open shell without login

`ctrl + alt + f5`

## dns change

```bash
# /etc/network/interfaces

# The primary network interface
dns-nameservers 185.51.200.2 178.22.122.100
```

```bash
sudo service networking restart
```

## Tmux

commands:

- create new session: `tmux new -s <session name>`

- connect to session: `tmux attach-session -t <session name>`

- disconnect from session: `ctrl+b + d`

- destroy session: `ctrl+d`

## Gnome

`sudo apt install gnome-tweak-tool chrome-gnome-shell`

Extensions:

- workspace thumbnails:

  https://extensions.gnome.org/extension/1516/workspace-switcher-popup-with-thumbnails/

- workspace like unity:

  https://extensions.gnome.org/extension/1485/workspace-matrix/

- no title bar:

  https://extensions.gnome.org/extension/1267/no-title-bar/

- hide top bar:

  https://extensions.gnome.org/extension/545/hide-top-bar/

- top bar back and text color changer

  https://extensions.gnome.org/extension/1011/dynamic-panel-transparency/

- workspace grid:

  https://extensions.gnome.org/extension/484/workspace-grid/

- move top bar to bottom:

  https://extensions.gnome.org/extension/949/bottompanel/

## Grub problem

1. To install and fix grub, you need Live CD or Live USB of Ubuntu
2. Once you load Live Ubuntu, Open Terminal and fire following commands to install boot-repair and let it fix the Grub
   `sudo add-apt-repository ppa:yannubuntu/boot-repair && sudo apt-get update`
   `sudo apt-get install -y boot-repair && boot-repair`
3. After installation, boot-repair will get automatically launched
4. Make sure to select “recommended repair” option to repair grub. Reboot
5. You will now have a Grub menu on boot, where you can choose from Ubuntu, and Windows

## disable sudo password for specific command

run `sudo EDITOR=vim visudo`

and add below line after  `%sudo ...` line

```
<user>  ALL=NOPASSWD: <command: /bin/systemctl>
```

## add windows to boot loader

```
sudo os-prober
sudo update-grub
```

## machine version

`cat /etc/*-release`

## machine config

- cpu: `lscpu`
- memory: `free -h`

## minimal curl

```bash
curl -i -H "Accept: text/html" 127.0.0.1:31001 -v
```

## vim replace all

```
:%s/foo/bar/g
```

## merge two directory

```
rsync -a <other/dir> <destination/dir>
```

## get all process with their threads

NLWP = threads

```
ps -eLf | less
```

