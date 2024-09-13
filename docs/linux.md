# Linux

## Links

- [Sudo password cache](https://apple.stackexchange.com/questions/10139/how-do-i-increase-sudo-password-remember-timeout#answer-51763)
- [Debian mirror sites](https://www.debian.org/mirror/list)
- [Vim readonly save problem](https://superuser.com/questions/694450/using-vim-to-force-edit-a-file-when-you-opened-without-permissions/785016#785016)
- [Start Ubuntu in console mode](https://askubuntu.com/a/859640)
- [Youcompleteme unavailable: requires Vim 8.1.2269+](https://github.com/ycm-core/YouCompleteMe/issues/3764#issuecomment-755816205)
- [Ubuntu <=> Debian](https://askubuntu.com/questions/445487/what-debian-version-are-the-different-ubuntu-versions-based-on/445496#445496)
- [Possible missing firmware](https://unix.stackexchange.com/questions/556946/possible-missing-firmware-lib-firmware-i915-for-module-i915/557015#557015)
- [Vim configuration](https://jadi.net/2020/05/vim-prat-3/)
- [Screen recorder](https://obsproject.com/wiki/unofficial-linux-builds#debian)
- [Useful commands cheatsheet](https://xmind.app/m/WwtB/)

## SSH

- Download to local:

  ```
  scp -[r]P <port> <user>@<ip>:<path/to/folder> <path/to/local>
  ```

- Upload to server:

  ```
  scp -[r]P <port> <source file> <username>@<destination server>:<destination directory>
  ```

- Generate ssh key:

  ```
  ssh-keygen -t rsa
  ssh-add
  ```

- List of private keys:

  ```
  ssh-add -l
  ```

- Access to public ssh key:

  ```
  cat ~/.ssh/id_rsa.pub
  ```

- Prevent SSH from disconnecting:

  ```shell
  # /etc/ssh/ssh_config or ~/.ssh/config
  ServerAliveInterval 60
  ```

## Compress & Extract

- .tgz:

  ```
  # Compress
  tar -czvf <file_name.tgz> </path/to/directory>
  tar -czvf <file_name.tgz> </path/to/directory>/.  # include hidden files
  tar -czvf <file_name.tgz> </path/to/file>

  # Extract
  tar -xzvf <file_name.tgz>
  tar -xzvf <file_name.tgz> -C </path/to/directory>

  # Split into multiple files
  split --bytes=<split_size: 10m> --suffix-length=4 --numeric-suffix <source_file.tgz> <destination_file.tgz.>

  # Extract from splitted files (tgz)
  cat <destination_file.tgz.*> | tar -xzvf -
  ```

- .zip:

  ```
  # Compress
  zip <filename.zip> <file>

  # Extract (`sudo apt install unzip`)
  unzip <file_name.zip>
  unzip '*.zip'
  ```

- .rar

  ```
  # Extract (sudo apt-get install unrar)
  unrar x -r </path/to/file.rar>
  ```

## Cron

1. Create a bash file that starts with `#!/bin/bash` and without the `.sh` filename suffix
2. Change the file to runnable mode with the `sudo chmod +x` command
3. ceate a soft link in the `/etc/cron.daily/` or add it to the `/etc/crontab`
5. Test for correct run: `run-parts --test /etc/cron.daily`

## Xmodmap

- Remove a key from a mod:

  ```
  xmodmap -e 'remove Mod1 = Alt_R'
  ```
- Add a key to a mod:

  ```
  xmodmap -e 'add Mod3 = Alt_R'
  ```

## Firewall

- Enable and disable firewall:

  ```
  sudo ufw enable/disable
  ```

- Get status of firewall and all available ports:

  ```
  sudo ufw status verbose
  ```

- Get list of apps that wanna firewall access:

  ```
  sudo ufw app list
  ```

- Set or get firewall access for port:

  ```
  sudo ufw allow <port>
  sudo ufw delete allow <port>
  ```

- Set or get firewall access for app:

  ```
  sudo ufw allow in "<app name>"
  sudo ufw delete allow in "<app name>"
  ```

## Add Proxy To Apt-Get

1. Go to https://free-proxy-list.net/ and find an free proxy address

2. Add below code to `/etc/apt/apt.conf`:

   ```
   # If your proxy has not password
   Acquire::http::Proxy "http://<yourproxyaddress>:<proxyport>";

   # If your proxy has password
   Acquire::http::Proxy "http://<username>:<password>@<proxyaddress>:<proxyport>";
   ```

## Remove Launcher Entry

1. Go to `~/.local/share/applications/` or `/usr/share/applications/`
2. Remove `<your application name: jetbrains-pycharm.desktop>`

## Networkmanager

- List of connections:

  ```
  nmcli connection
  ```
- Change DNS:

  ```
  nmcli connection modify <connection name> ipv4.dns "<dns one:8.8.8.8> <dns two:8.8.4.4>"
  ```
- Connection down (need to restart):

  ```
  nmcli connection down <connection name>
  ```
- Connection up (need to restart):

  ```
  nmcli connection up <connection name>
  ```

## Tmux

- Create new terminal:

  ```
  tmux
  ```

- Split current terminal vertically:

  ```
  ctrl+b %
  ```

- Split current terminal horizontally:

  ```
  ctrl+b "
  ```

- New window (tab):

  ```
  ctrl+b c
  ```

- Maximize and minimize terminal:

  ```
  ctrl+b z
  ```

- Switch between terminals:

  ```
  ctrl+b o
  ```

- Create new session:

  ```
  tmux new -s <session_name>
  ```

- Connect to session:

  ```
  tmux attach-session -t <session_name>
  ```

- Disconnect from session:

  ```
  ctrl+b + d
  ```

- Destroy session:

  ```
  ctrl+d
  ```

## Grub

- Edit configs:

  ```
  sudo vim /etc/default/grub
  sudo update-grub
  ```

- Grub Problem:

  1. To install and fix grub, you need Live CD or Live USB of Ubuntu

  2. Once you load Live Ubuntu, Open Terminal and fire following commands to install boot-repair and let it fix the Grub

     ```
     sudo add-apt-repository ppa:yannubuntu/boot-repair && sudo apt-get update
     sudo apt-get install -y boot-repair && boot-repair
     ```

  3. After installation, boot-repair will get automatically launched

  4. Make sure to select “recommended repair” option to repair grub. Reboot

  5. You will now have a Grub menu on boot, where you can choose from Ubuntu, and Windows

- Add Windows to boot loader:

  ```
  sudo os-prober
  sudo update-grub
  ```

## Disable Sudo Password

1. Run:

   ```
   sudo EDITOR=vim visudo
   ```

2. And add below line after  `%sudo` line:

   ```
   # For specific user
   <username>	ALL=(ALL) NOPASSWD: <command: /bin/systemctl>

   # For all users
   ALL	ALL=(ALL) NOPASSWD: <command: /bin/systemctl>
   ```

## Machine

- Version:

  ````
  cat /etc/*-release
  ````

- CPU:

  ```
  lscpu
  ```

- Memory:

  ```
  free -h
  ```

- Disk space:

  ```
  # Simple
  df -h

  # Advanced
  ncdu
  ```

- Install package:

  ```
  # .dev
  sudo dpkg -i path/to/file.deb
  sudo apt-get install -f

  # .rpm
  sudo alien -i path/to/file.rpm
  ```

- Boot type:

  ```
  cat /etc/fstab

  # If there is a line like `UUID=xxx /boot/efi ntfs defaults 0 1`, it means the system boot mode is UEFI, otherwise, it is Legacy BIOS
  ```

- Kernel logs:

  ```
  dmesg -l err
  ```

## Nvidia Driver

1. First we will install the proper driver:

   ```
   sudo apt install nvidia-detect
   nvidia-detect
   sudo apt install <suggested_package_from_previous_step>
   ```

2. After restarting the system driver should work properly, if not we will install the below packages:

   ```
   sudo apt-get install bumblebee bumblebee-nvidia linux-headers-generic
   ```

3. Now each time that we want to use the NVIDIA GPU should run the following command! (While the following command is runnuing we can run every program that we want to use NVIDIA GPU)

   ```
   sudo optirun nvidia-settings -c :8
   ```

## Gnome

- Reset an extension configs:

  ```
  dconf reset -f /org/gnome/shell/extensions/<extension_name>
  ```

## Mount & Partition

- See disk usage:

  ```
  sudo lsblk
  ```

-  Create primary partition:

  ```
  sudo fdisk /dev/sda

  ... Command (m for help): n
  ... Select (default p): p
  ... Partition number (1-4, default 1):
  ... First sector (46483456-62914559, default 46483456):
  ... Last sector, +/- sectors or +/-size{K,M,G,T,P} (46483456-62914559, default 62914559):

  ... Command (m for help): w
  ```

- Create file system:

  ```
  sudo mkfs.ext4 /dev/sda1
  ```

- Mount partition

  ```
  sudo mkdir /sample_dir

  sudo mount /dev/sda1 /sample_dir  # for mount
  sudo umount /sample_dir  # for unmount
  ```

- Mount directory

  ```
  sudo mkdir /source_dir
  sudo mkdir /destination_dir

  sudo mount --bind /source_dir /destination_dir
  ```

- Determine the file system type:

  ```
  sudo fsck -N /dev/sda1
  ```

## `Alt+Shift+<any_other_key>` doesn't work:

The problem is related to the change-layout shortcut, by default it is set to Alt+Shift, for this reason, the system intercepts it for itself and doesn't let it reach some programs like Pycharm or VSCode.

To solve, update `/etc/default/keyboard` and replace

```
XKBOPTIONS="grp:alt_shift_toggle,grp_led:scroll"
```

with

```
XKBOPTIONS="grp:super_space_toggle,grp_led:scroll"
```

## Other

- Minimal Curl:

  ```
  curl -i -H "Accept: text/html" 127.0.0.1:31001 -v
  ```

- Vim replace all:

  ```
  :%s/foo/bar/g
  ```

- Open shell without login:

  ```
  ctrl + alt + f5
  ```
