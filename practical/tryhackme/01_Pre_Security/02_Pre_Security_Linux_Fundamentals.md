# Pre-Security 
---
# Linux Fundamentals - Commands

Linux is a powerful open-source operating system widely used in servers, development environments, cybersecurity, and embedded systems. At its core, Linux is built around the Unix philosophy of simplicity and modularity, using a command-line interface to manage files, processes, and system resources. Understanding Linux fundamentals includes navigating the filesystem, managing permissions, using essential commands, editing configuration files, and handling user and group management. Mastery of these basics lays the foundation for more advanced tasks like scripting, system administration, and network troubleshooting. Whether you're pursuing IT, cybersecurity, or software development, a solid grasp of Linux is an essential skill.


### echo
Prints text or variables to the terminal.

**Example:**  
```bash
echo Hello, world!
```
### Whoami 
Displays the username of the current user..
```bash
whoami
```

<img src="./pre-security-screenshots/Linux01.jpg" width="800"  alt="Linux 1">

---

`ls` — Lists files and directories (e.g., `ls -l`)  
`cd` — Changes the current directory (e.g., `cd /home/user`)  
`cat` — Displays file content (e.g., `cat file.txt`)  
`pwd` — Prints the current directory (e.g., `pwd`)  

<img src="./pre-security-screenshots/Linux02.jpg" width="800"  alt="Linux 2">

---

### Find

`find` — Searches for files and directories in a directory hierarchy (e.g., `find .`)  
`find -name "*.txt"` — Finds files with a `.txt` extension (useful when you only know the file type) (e.g., `find . -name "*.txt"`)  
`find -type f` — Finds only files (e.g., `find . -type f`)  
`find -type d` — Finds only directories (e.g., `find . -type d`)  
`find -exec` — Executes a command on found items (e.g., `find . -name "*.log" -exec rm {} \;`)  

<img src="./pre-security-screenshots/Linux03.jpg" width="800"  alt="Linux 3">

---

### Grep

`grep` — Searches for a pattern in files (e.g., `grep "hello" file.txt`)  
`grep -i` — Ignores case while searching (e.g., `grep -i "hello" file.txt`)  
`grep -r` — Recursively searches in directories (e.g., `grep -r "main" ./src`)  
`grep -v` — Inverts the match; shows lines that do *not* contain the pattern (e.g., `grep -v "error" file.txt`)  
`grep -n` — Shows line numbers along with matching lines (e.g., `grep -n "TODO" file.txt`)  
`grep -l` — Lists only filenames with matches (e.g., `grep -l "function" *.py`)  

<img src="./pre-security-screenshots/Linux04.jpg" width="800"  alt="Linux 4">

---

### Introduction to Shell Operators

`&` — Runs a command in the background (e.g., `sleep 10 &`)  
`&&` — Runs the next command only if the previous one succeeds (e.g., `mkdir test && cd test`)  
`>` — Redirects output to a file, replacing its contents (e.g., `echo "Hello" > file.txt`)  
`>>` — Appends output to a file without replacing existing content (e.g., `echo "More" >> file.txt`)  

<img src="./pre-security-screenshots/Linux05.jpg" width="800"  alt="Linux 5">

---

### Help Commands in Linux

`--help` — Displays a brief help message about how to use a command (e.g., `ls --help`)  
`man` — Opens the manual page for a command with detailed documentation (e.g., `man ls`)  

<img src="./pre-security-screenshots/Linux06.jpg" width="400"  alt="Linux 6">
<img src="./pre-security-screenshots/Linux07.jpg" width="400"  alt="Linux 7">

---

### Common File and Directory Commands

`touch` — Creates a new file (e.g., `touch file.txt`)  
`mkdir` — Creates a new directory/folder (e.g., `mkdir my_folder`)  
`cp` — Copies a file or directory (e.g., `cp file.txt backup.txt`)  
`mv` — Moves or renames a file or directory (e.g., `mv file.txt ../`)  
`rm` — Removes/deletes a file (e.g., `rm file.txt`)  
`rm -r` — Removes a directory and its contents recursively (e.g., `rm -r my_folder`)  
`file` — Determines the type of a file (e.g., `file image.png`)  

---

### Understanding File Permissions and `ls -lh` Output in Linux

`ls -lh` — Lists files/directories with detailed info in a human-readable format (sizes in KB, MB, etc.)  

| Position | Meaning                                 | Example                  |
| -------- | --------------------------------------- | ------------------------ |
| `-`      | File type (`-` = file, `d` = directory) | `-` means a regular file |
| `r`      | Read permission                         | File can be read         |
| `w`      | Write permission                        | File can be modified     |
| `x`      | Execute permission                      | File can be run/executed |

Permissions are grouped in **three sets of three**:

- **User (owner)** permissions: `rwx` (read, write, execute)  
- **Group** permissions: `r-x` (read, no write, execute)  
- **Others** permissions: `r--` (read only)  

<img src="./pre-security-screenshots/Linux08.jpg" width="800"  alt="Linux 8">

---

### Users and Groups in Linux: Differences and Switching Users

Linux permissions allow granular control: while a single user owns a file, groups can have their own set of permissions on the same file without affecting the owner.

**Real-world example:**  
A web server user needs read/write permissions for web files, but hosting companies want customers to upload files securely without giving them full webserver permissions — improving security.

### Switching Between Users

The `su` command lets you switch users easily. To switch, you need:

- The username you want to switch to  
- The password of that user  

Example usage with login shell:

```bash
su username        # Switch user, but keep root's PATH
su -l username     # Switch user and use username's environment
```

<img src="./pre-security-screenshots/Linux09.jpg" width="800"  alt="Linux 9">

---

### Using SSH to Login to Your Linux Machine

The syntax to use SSH is very simple. You only need two things:

1. The IP address of the remote machine  
2. Valid credentials (username and password) for a user on that machine  

For this example, you will log in as the user `tryhackme` with the password `tryhackme`.

To connect via SSH, use the following format:

```bash
ssh username@IP_address
```

<img src="./pre-security-screenshots/Linux10.jpg" width="800"  alt="Linux 10">

---

### Common Directories

#### /etc/
Configuration files and directories
- `passwd` — User account information
- `shadow` — Secure user password information
- `sudoers` — Permissions for sudo users
- `sudoers.d/` — Directory for additional sudoers configurations

#### /var/
Variable data files (logs, backups, caches)
- `backups/` — Backup files
- `log/` — System log files
- `opt/` — Optional application data
- `tmp/` — Temporary files (persistent across reboots)

#### /root/
Root user's home directory

#### /tmp/
Temporary files directory (cleared on reboot)


```bash
cd /etc
ls
```
---

### Nano
#### Common Nano Commands

`nano filename` — Opens or creates a file named `filename` for editing  
`Ctrl + O` — Saves (writes out) the changes to the file  
`Ctrl + X` — Exits Nano (prompts to save if there are unsaved changes)  
`Ctrl + K` — Cuts the current line  
`Ctrl + U` — Pastes the last cut line  
`Ctrl + W` — Searches for text inside the file  
`Ctrl + G` — Opens Nano’s help menu  

<img src="./pre-security-screenshots/Linux11.jpg" width="800"  alt="Linux 11">

---

### Vim

#### Common VIM Commands

`vim filename` — Opens or creates a file named `filename` for editing  
`i` — Enters **insert mode** to start typing text  
`Esc` — Returns to **normal mode** (command mode)  
`:w` — Saves (writes) the file  
`:q` — Quits VIM (only works if no changes)  
`:q!` — Quits VIM without saving changes  
`:wq` or `:x` — Saves and quits VIM  
`dd` — Deletes (cuts) the current line  
`p` — Pastes the last deleted or copied text  
`/text` — Searches for “text” in the file  
`u` — Undoes the last change  

<img src="./pre-security-screenshots/Linux12.jpg" width="800"  alt="Linux 12">

---

### `wget` Command Example

`wget https://assets.tryhackme.com/additional/linux-fundamentals/part3/myfile.txt`  
— Downloads the file `myfile.txt` from the specified URL and saves it in the current working directory.

**Breakdown:**
- `wget` — Command-line tool to download files from the web
- `https://assets.tryhackme.com/.../myfile.txt` — Direct URL to the file you want to download

**Result:**  
A file named `myfile.txt` will be saved in your current directory.

---

### `scp` Command Example

`scp important.txt ubuntu@192.168.1.30:/home/ubuntu/transferred.txt`  
— Securely copies the local file `important.txt` to a remote machine at IP `192.168.1.30` using the username `ubuntu`, and saves it as `transferred.txt` in `/home/ubuntu/`.

**Breakdown:**
- `scp` — Secure copy command (uses SSH)
- `important.txt` — Source file on your **local** machine
- `ubuntu@192.168.1.30:` — Remote user (`ubuntu`) and IP address of the destination machine
- `/home/ubuntu/transferred.txt` — Full path and new name for the copied file on the **remote** machine

**Note:** You may be prompted for the password of the remote user (`ubuntu`).

---


# 🧠 Understanding Linux Processes

## 🔹 What Are Processes?

Processes are running programs on a Linux system, each managed by the kernel. Every process is assigned a unique Process ID (PID), which is given in the order processes start. For example, the 60th process will usually have a PID of 60.

---

## 🔍 Viewing Processes

### View User Session Processes
To see running processes in your current session:
```bash
ps
```
<img src="./pre-security-screenshots/Linux13.jpg" width="800"  alt="Linux 13">

This will display:
- PID
- TTY (terminal)
- Time (CPU usage time)
- Command (program running)

### View All System Processes
To view every process on the system, including those from other users:
```bash
ps aux
```

This command lists:
- User who owns the process
- CPU and memory usage
- PID and other stats
- Full command being run

---

## 📊 Real-Time Process Monitoring

Use the `top` command to see live process activity:
```bash
top
```
<img src="./pre-security-screenshots/Linux14.jpg" width="800"  alt="Linux 14">

- Updates every 10 seconds by default.
- You can scroll to explore more processes.
- Useful for monitoring CPU and memory usage in real time.

---

## 🛠️ Managing Processes

To send signals to processes (e.g., to terminate), use the `kill` command with a PID.

Example:
```bash
kill 1337
```

### Common Signals
- `SIGTERM`: Gracefully stops a process (default).
- `SIGKILL`: Forcefully stops a process (no cleanup).
- `SIGSTOP`: Pauses (suspends) a process.

---

## ⚙️ How Processes Start

Linux uses **namespaces** to isolate resources between processes. Each namespace controls access to system resources like CPU, memory, and devices.

- The first process started during boot is PID 0.
- The system then launches `init` (like `systemd` on Ubuntu), which manages other processes.
- Programs started after boot become **child processes** of `systemd`.

---

## 🚀 Starting Services on Boot

To start or manage services like a web server (e.g., Apache), use `systemctl`:

### Basic Commands
```bash
systemctl start apache2
systemctl stop apache2
systemctl enable apache2  # Start on boot
systemctl disable apache2 # Don’t start on boot
```

---

## 🔄 Background & Foreground Processes

### Running in Foreground
Most commands run in the foreground by default:
```bash
echo "Hello World"
```

### Running in Background
Use `&` to run a command in the background:
```bash
echo "Hello World" &
```
<img src="./pre-security-screenshots/Linux15.jpg" width="800"  alt="Linux 15">

This allows you to continue using the terminal while the process runs.

### Suspending Processes
You can pause a process with `Ctrl + Z`.

---

## 🔁 Resuming Background Processes

To bring a background/suspended process back to the foreground:
```bash
fg
```

This resumes terminal interaction with the process.

---

## ✅ Summary

| Command | Purpose |
|--------|---------|
| `ps` | View current session processes |
| `ps aux` | View all system processes |
| `top` | Real-time process monitoring |
| `kill PID` | Send signal to stop a process |
| `systemctl start|stop|enable|disable` | Manage services |
| `&`, `Ctrl + Z`, `fg` | Backgrounding and foregrounding processes |

---
## 🛠️ Maintaining Your System: Automation

Automation is a powerful way to ensure certain tasks run after the system boots — such as:
- Running custom commands
- Backing up files
- Launching your favorite apps like **Spotify** or **Google Chrome**

### 📌 What Is `cron` and `crontab`?

The `cron` process is responsible for running scheduled tasks in Linux. You interact with it using a tool called `crontab`.

- **cron** starts automatically at boot.
- **crontab** is the configuration file that contains a list of jobs to be executed at specified times.

### 📅 Crontab Format

A `crontab` file contains lines with **6 fields**:

| Field | Meaning                          |
|-------|----------------------------------|
| MIN   | Minute (0-59)                    |
| HOUR  | Hour (0-23)                      |
| DOM   | Day of the Month (1-31)          |
| MON   | Month (1-12)                     |
| DOW   | Day of the Week (0-6, Sun=0)     |
| CMD   | The command to be executed       |


#### 📁 Example: Backup Every 12 Hours

To backup the user `cmnatic`'s `Documents` directory every 12 hours:

```bash
0 */12 * * * cp -R /home/cmnatic/Documents /var/backups/
```
### 🧪 Real-World Example: Auto Backup Every Night

Let's say we want to back up the entire `/var/www` directory every night at **2:30 AM** and store the backup in `/var/backups`.

#### ✏️ Crontab Entry
```bash
30 2 * * * tar -czf /var/backups/www-$(date +\%F).tar.gz /var/www
```
**Each day, it creates a new file with the current date. Over several days, your /var/backups/ directory might look like this:**

```
/var/backups/
├── www-2025-06-13.tar.gz
├── www-2025-06-14.tar.gz
├── www-2025-06-15.tar.gz
```
--- 
## 🛠️ Maintaining Your System: Logs

System logs are crucial for understanding what is happening on a Linux system. These logs provide insight into services, security, user activity, and system performance.

### 📁 Where Are Logs Stored?

All major logs are stored in the `/var/log/` directory:

```bash
cd /var/log/
ls
```

<img src="./pre-security-screenshots/Linux16.jpg" width="800"  alt="Linux 16">

### 📑 Why Logs Matter for System Health & Security

System and service logs are essential for:

- 🛡️ Monitoring system **health and performance**
- 🧠 Diagnosing issues with services like web servers
- 🔍 Investigating suspicious or unauthorized activity
- 🛠️ Debugging software errors and system failures

For example, web server logs such as Apache2 or Nginx maintain:

#### 🔎 Types of Web Server Logs

| Log File       | Description |
|----------------|-------------|
| **access.log** | Logs every incoming HTTP request — includes IP address, requested resource, browser info, and status codes |
| **error.log**  | Records server-side errors — useful for debugging configuration issues or failed script executions |

#### Example: View Apache2 Access Log

```bash
sudo tail -f /var/log/apache2
ls
```
<img src="./pre-security-screenshots/Linux17.jpg" width="800"  alt="Linux 17">

<br><br>
> **Note:** These notes document hands-on learning from the TryHackMe *Pre-Security* path. The exercises cover fundamental cybersecurity topics, including Linux basics, networking concepts, and web technologies. This document is intended for personal learning, revision, and ethical skill development. All screenshots, commands, and actions are for educational purposes only.  
> — Compiled by moh4med404 | Curious Mind | Cybersecurity Enthusiast 