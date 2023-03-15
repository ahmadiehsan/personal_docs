# Linux

## disk space

`df -h`

## Install .deb package

```
sudo dpkg -i path/to/deb/file.deb
sudo apt-get install -f
```

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
# compress (tgz)
tar -czvf <file_name.tgz> </path/to/directory>
tar -czvf <file_name.tgz> </path/to/directory>/.	# include hidden files
tar -czvf <file_name.tgz> </path/to/file>

# extract (tgz)
tar -xzvf <file_name.tgz>
tar -xzvf <file_name.tgz> -C </path/to/directory>

# compress (zip)
zip <filename.zip> <file>

# extract (zip)  # sudo apt install unzip
unzip <file_name.zip>
unzip '*.zip'

# split into multiple files (tgz)
split --bytes=<split_size: 10m> --suffix-length=4 --numeric-suffix <source_file.tgz> <destination_file.tgz.>

# extract from splitted files (tgz)
cat <destination_file.tgz.*> | tar -xzvf -

# extract (rar)  # sudo apt-get install unrar
unrar x -r </path/to/file.rar>
```

## Cron

1. create a bash file that starts with `#!/bin/bash` and without the `.sh` filename suffix
2. change the file to runnable mode with the `sudo chmod +x` command
3. create a soft link in the `/etc/cron.daily/`
4. or add it to the `/etc/crontab`
5. test for correct run: `run-parts --test /etc/cron.daily`

## xmodmap

- remove a key from a mod: `xmodmap -e 'remove Mod1 = Alt_R'`
- add a key to a mod: `xmodmap -e 'add Mod3 = Alt_R'`

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

## NetworkManager

- list of connections: `nmcli connection`
- change DNS: `nmcli connection modify <connection name> ipv4.dns "<dns one:8.8.8.8> <dns two:8.8.4.4>"`
- connection down (need for restart): `nmcli connection down <connection name>`
- connection up (need for restart): `nmcli connection up <connection name>`

## Tmux

Commands:

- create new terminal: `tmux`

- split current terminal vertically: `ctrl+b %`

- split current terminal horizontally: `ctrl+b "`

- maximize and minimize terminal: `ctrl+b z`

- switch between terminals: `ctrl+b o`

- create new session: `tmux new -s <session name>`

- connect to session: `tmux attach-session -t <session name>`

- disconnect from session: `ctrl+b + d`

- destroy session: `ctrl+d`

`~/.tmux.conf` file:

- colored shell: `set -g default-terminal "screen-256color"`
- mouse activation: `set -g mouse on`

## Gnome

`sudo apt install gnome-tweak-tool chrome-gnome-shell`

Extensions:

- workspace thumbnails:

  https://extensions.gnome.org/extension/1516/workspace-switcher-popup-with-thumbnails/

- workspace like unity:

  https://extensions.gnome.org/extension/1485/workspace-matrix/

- Drop Down Terminal

  https://extensions.gnome.org/extension/1509/drop-down-terminal-x/
  
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

## Grub

### Edit

```
sudo vim /etc/default/grub
sudo update-grub
```

### Grub problem

1. To install and fix grub, you need Live CD or Live USB of Ubuntu
2. Once you load Live Ubuntu, Open Terminal and fire following commands to install boot-repair and let it fix the Grub
   `sudo add-apt-repository ppa:yannubuntu/boot-repair && sudo apt-get update`
   `sudo apt-get install -y boot-repair && boot-repair`
3. After installation, boot-repair will get automatically launched
4. Make sure to select “recommended repair” option to repair grub. Reboot
5. You will now have a Grub menu on boot, where you can choose from Ubuntu, and Windows

## disable sudo password for specific or all commands

run `sudo EDITOR=vim visudo`

and add below line after  `%sudo ...` line

```
<user>  ALL=NOPASSWD: <command: /bin/systemctl>
<user>  ALL=(ALL) NOPASSWD: ALL
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

## Kernel logs

```
dmesg -l err
```

## NVIDIA driver

First we will install the proper driver:

```
sudo apt install nvidia-detect
nvidia-detect
sudo apt install <suggested_package_from_previous_step>
```

After restarting the system driver should work properly, if not we will install the below packages:

```
sudo apt-get install bumblebee bumblebee-nvidia linux-headers-generic
```

Now each time that we want to use the NVIDIA GPU should run the bellow command! (While the below command is run we can run every program that we want to use NVIDIA GPU)

```
sudo optirun nvidia-settings -c :8
```

## Mount and Partition

- See Disk Usage:

  ```
  sudo lsblk
  ```

-  Create Primary Partition:

  ```
  sudo fdisk /dev/sda
  
  ... Command (m for help): n
  ... Select (default p): p
  ... Partition number (1-4, default 1):
  ... First sector (46483456-62914559, default 46483456):
  ... Last sector, +/- sectors or +/-size{K,M,G,T,P} (46483456-62914559, default 62914559):
  
  ... Command (m for help): w
  ```

- Create File system:

  ```
  sudo mkfs.ext4 /dev/sda1
  ```

- Mount Partition

  ```
  sudo mkdir /sample_dir
  
  sudo mount /dev/sda1 /sample_dir  # for mount
  sudo umount /sample_dir  # for unmount
  ```
  
- Mount Directory

  ```
  sudo mkdir /source_dir
  sudo mkdir /destination_dir
  
  sudo mount --bind /source_dir /destination_dir
  ```

- Determine the File System Type:

  ```
  sudo fsck -N /dev/sda1
  ```
