
# Cybersecurity 101 
---
# Offensive Security Tooling: Hydra

**Hydra** is an online brute-force password-cracking tool used to quickly attempt logins to systems using various protocols. It's commonly used for testing the strength of authentication services such as SSH, FTP, HTTP forms, and more.

#### How Hydra Works

Hydra automates the process of guessing passwords by using a **password list** to try many combinations rapidly. Rather than attempting login guesses manually, Hydra can perform these attempts efficiently across multiple services.

#### Supported Protocols

Hydra supports a wide range of protocols, including (but not limited to):

- SSH (v1 and v2), FTP, Telnet, RDP, HTTP/HTTPS (GET, POST, FORM), SMB, SNMP (v1/v2/v3), SMTP, IMAP, MySQL, PostgreSQL, MS-SQL, Oracle, MongoDB, VNC, XMPP, IRC, and more.

> For a full list of supported protocols, see the [official THC-Hydra GitHub repository](https://github.com/vanhauser-thc/thc-hydra).

#### Why Strong Passwords Matter

Weak passwords such as `admin:password` are easily guessable using Hydra and publicly available password lists. Many applications (e.g., CCTV systems, web frameworks) use default credentials that should be changed immediately.

A strong password should:
- Be longer than 8 characters
- Include uppercase, lowercase, numbers, and special characters
- Avoid common patterns or dictionary words

### Installing Hydra

Hydra comes **pre-installed** in:

- **AttackBox**
- **Kali Linux** distributions (browser or local)

To install on other Linux distributions:

- **Ubuntu/Debian**:  
  ```bash
  sudo apt install hydra
  ```

## Hydra Commands

The options we pass into Hydra depend on which service (protocol) we’re attacking. For example, if we wanted to brute force FTP with the username being `user` and a password list being `passlist.txt`, we’d use the following command: `hydra -l user -P passlist.txt ftp://MACHINE_IP`

For this deployed machine, here are the commands to use Hydra on SSH and a web form (POST method).

#### SSH
``` bash 
hydra -l <username> -P <full path to pass> MACHINE_IP -t 4 ssh
```

| Option | Description                            |
|--------|----------------------------------------|
| `-l`   | Specifies the (SSH) username for login |
| `-P`   | Indicates a list of passwords          |
| `-t`   | Sets the number of threads to spawn    |


For example, `hydra -l root -P passwords.txt MACHINE_IP -t 4 ssh` will run with the following arguments:

- Hydra will use `root` as the username for `ssh`
- It will try the passwords in the `passwords.txt` file
- There will be four threads running in parallel as indicated by `-t 4` 

#### Post Web Form

We can use Hydra to brute force web forms too. You must know which type of request it is making; GET or POST methods are commonly used. You can use your browser’s network tab (in developer tools) to see the request types or view the source code.

```bash 
sudo hydra <username> <wordlist> MACHINE_IP http-post-form "<path>:<login_credentials>:<invalid_response>"
```

| Option               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `-l`                 | The username for (web form) login                                           |
| `-P`                 | The password list to use                                                    |
| `http-post-form`     | Specifies that the form type is POST                                        |
| `<path>`             | The login page URL, e.g., `login.php`                                       |
| `<login_credentials>`| The username and password fields, e.g., `username=^USER^&password=^PASS^`   |
| `<invalid_response>` | Part of the server response shown when login fails                          |
| `-V`                 | Verbose output for every attempt                                            |


Below is a more concrete example Hydra command to brute force a POST login form:

```bash 
hydra -l <username> -P <wordlist> MACHINE_IP http-post-form "/:username=^USER^&password=^PASS^:F=incorrect" -V
```
- The login page is only `/`, i.e., the main IP address.
- The `username` is the form field where the username is entered
- The specified username(s) will replace `^USER^`
- The `password` is the form field where the password is entered
- The provided passwords will be replacing `^PASS^`
- Finally, `F=incorrect` is a string that appears in the server reply when the login fails

---
> **Note:** These notes document hands-on learning from the TryHackMe *Cybersecurity 101* path. The exercises cover fundamental cybersecurity topics, including Linux basics, networking concepts, and web technologies. This document is intended for personal learning, revision, and ethical skill development. All screenshots, commands, and actions are for educational purposes only.  
> — Compiled by moh4med404 | Curious Mind | Cybersecurity Enthusiast