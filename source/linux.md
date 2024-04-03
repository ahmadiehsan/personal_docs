# Linux

## Links

- [Reset Gnome desktop](http://ubuntuhandbook.org/index.php/2018/06/reset-gnome-desktop-ubuntu-18-04/)
- [Sudo password cache](https://apple.stackexchange.com/questions/10139/how-do-i-increase-sudo-password-remember-timeout#answer-51763)
- [Debian mirror sites](https://www.debian.org/mirror/list)
- [Vim readonly save problem](https://superuser.com/questions/694450/using-vim-to-force-edit-a-file-when-you-opened-without-permissions/785016#785016)
- [Start Ubuntu in console mode](https://askubuntu.com/a/859640)
- [Youcompleteme unavailable: requires Vim 8.1.2269+](https://github.com/ycm-core/YouCompleteMe/issues/3764#issuecomment-755816205)
- [Ubuntu &Lt;=&Gt; Debian](https://askubuntu.com/questions/445487/what-debian-version-are-the-different-ubuntu-versions-based-on/445496#445496)
- [Possible missing firmware](https://unix.stackexchange.com/questions/556946/possible-missing-firmware-lib-firmware-i915-for-module-i915/557015#557015)
- [Vim configuration](https://jadi.net/2020/05/vim-prat-3/)
- [Screen recorder](https://obsproject.com/wiki/unofficial-linux-builds#debian)
- [Useful commands cheatsheet](https://xmind.app/m/WwtB/)

## Disk Space

- simple: `df -h`
- advanced: `ncdu`

## Install Package

- .deb

  ```
  sudo dpkg -i path/to/file.deb
  sudo apt-get install -f
  ```

- .rpm

  ```
  sudo alien -i path/to/file.rpm
  ```

## Check Boot Type

1. Run `cat /etc/fstab`

2. If there is a line like this, it means the system boot mode is UEFI, otherwise, it is Legacy BIOS

   ```
   UUID=xxx /boot/efi ntfs defaults 0 1
   ```

## Ssh

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

## Contrib / Non-Free Repo

```
# /etc/apt/sources.list

deb http://deb.debian.org/debian/ buster main contrib non-free
deb-src http://deb.debian.org/debian/ buster main contrib non-free

deb http://security.debian.org/debian-security buster/updates main contrib non-free
deb-src http://security.debian.org/debian-security buster/updates main contrib non-free

deb http://deb.debian.org/debian/ buster-updates main contrib non-free
deb-src http://deb.debian.org/debian/ buster-updates main contrib non-free
```

## Compress And Extract

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

## Xmodmap

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

## Add Proxy To Apt-Get

1. go to https://free-proxy-list.net/ and find an free proxy address

2. add below code to `/etc/apt/apt.conf`

   - if your proxy has not password

     `Acquire::http::Proxy "http://<yourproxyaddress>:<proxyport>";`

   - if your proxy has password

     `Acquire::http::Proxy "http://<username>:<password>@<proxyaddress>:<proxyport>";`

## Remove Launcher Entry

1. go to
   - `~/.local/share/applications/` if you create entry for you user only
   - `/usr/share/applications/` if you create entry for all users
2. remove `<your application name: jetbrains-pycharm.desktop>`

## Open Shell Without Login

`ctrl + alt + f5`

## Networkmanager

- list of connections: `nmcli connection`
- change DNS: `nmcli connection modify <connection name> ipv4.dns "<dns one:8.8.8.8> <dns two:8.8.4.4>"`
- connection down (need for restart): `nmcli connection down <connection name>`
- connection up (need for restart): `nmcli connection up <connection name>`

## Tmux

Commands:

- create new terminal: `tmux`

- split current terminal vertically: `ctrl+b %`

- split current terminal horizontally: `ctrl+b "`

- new window (tab): `ctrl+b c`

- maximize and minimize terminal: `ctrl+b z`

- switch between terminals: `ctrl+b o`

- create new session: `tmux new -s <session name>`

- connect to session: `tmux attach-session -t <session name>`

- disconnect from session: `ctrl+b + d`

- destroy session: `ctrl+d`

## Gnome

Activate NumLock in the login screen for GDM by default:

```shell
gsettings set org.gnome.desktop.peripherals.keyboard numlock-state true
```

Additional packages:

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

### Grub Problem

1. To install and fix grub, you need Live CD or Live USB of Ubuntu
2. Once you load Live Ubuntu, Open Terminal and fire following commands to install boot-repair and let it fix the Grub
   `sudo add-apt-repository ppa:yannubuntu/boot-repair && sudo apt-get update`
   `sudo apt-get install -y boot-repair && boot-repair`
3. After installation, boot-repair will get automatically launched
4. Make sure to select “recommended repair” option to repair grub. Reboot
5. You will now have a Grub menu on boot, where you can choose from Ubuntu, and Windows

## Disable Sudo Password

1. run `sudo EDITOR=vim visudo`

2. and add below line after  `%sudo` line

   - For specific user

     ```
     <username>	ALL=(ALL) NOPASSWD: <command: /bin/systemctl>
     ```

   - For all users

     ```
     ALL	ALL=(ALL) NOPASSWD: <command: /bin/systemctl>
     ```

## Add Windows To Boot Loader

```
sudo os-prober
sudo update-grub
```

## Machine Version

`cat /etc/*-release`

## Machine Config

- cpu: `lscpu`
- memory: `free -h`

## Minimal Curl

```bash
curl -i -H "Accept: text/html" 127.0.0.1:31001 -v
```

## Vim Replace All

```
:%s/foo/bar/g
```

## Merge Two Directory

```
rsync -a <other/dir> <destination/dir>
```

## Get All Process With Their Threads

NLWP = threads

```
ps -eLf | less
```

## Kernel Logs

```
dmesg -l err
```

## Alt+Shift+<any_other_key> doesn't work

The problem is related to the change-layout shortcut, by default it is set to Alt+Shift, for this reason, the system intercepts it for itself and doesn't let it reach some programs like Pycharm or VSCode.

To solve, update `/etc/default/keyboard` and replace

```
XKBOPTIONS="grp:alt_shift_toggle,grp_led:scroll"
```

With

```
XKBOPTIONS="grp:super_space_toggle,grp_led:scroll"
```

## Nvidia Driver

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

## Mount And Partition

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
