# Cybersecurity 101 
---
# John the Ripper Basics

#### What are Hashes?

A hash is a way of taking a piece of data of any length and representing it in another fixed-length form. This process masks the original value of the data. The hash value is obtained by running the original data through a hashing algorithm. Many popular hashing algorithms exist, such as MD4, MD5, SHA1 and NTLM. Let’s try and show this with an example:

If we take “polo”, a string of four characters, and run it through an MD5 hashing algorithm, we end up with an output of `b53759f3ce692de7aff1b5779d3964da`, a standard 32-character MD5 hash.

Likewise, if we take “polomints”, a string of 9 characters, and run it through the same MD5 hashing algorithm, we end up with an output of `584b6e4f4586e136bc280f27f9c64f3b`, another standard 32-character MD5 hash.

#### What Makes Hashes Secure?

Hashing functions are designed as one-way functions. In other words, it is easy to calculate the hash value of a given input; however, it is a hard problem to find the original input given the hash value. In simple terms, a hard problem quickly becomes computationally infeasible in computer science. This computational problem has its roots in mathematics as P vs NP.

In computer science, P and NP are two classes of problems that help us understand the efficiency of algorithms:

- **P (Polynomial Time):** Class P covers the problems whose solution can be found in polynomial time. Consider sorting a list in increasing order. The longer the list, the longer it would take to sort; however, the increase in time is not exponential.
- **NP (Non-deterministic Polynomial Time):** Problems in the class NP are those for which a given solution can be checked quickly, even though finding the solution itself might be hard. In fact, we don’t know if there is a fast algorithm to find the solution in the first place.

While this is a fascinating mathematical concept that proves fundamental to computing and cryptography, it is entirely outside the scope of this room. But abstractly, the algorithm to hash the value will be “P” and can, therefore, be calculated reasonably. However, an “un-hashing” algorithm would be “NP” and intractable to solve, meaning that it cannot be computed in a reasonable time using standard computers.


#### Where John the Ripper Comes in

Even though the algorithm is not feasibly reversible, that doesn’t mean cracking the hashes is impossible. If you have the hashed version of a password, for example, and you know the hashing algorithm, you can use that hashing algorithm to hash a large number of words, called a dictionary. You can then compare these hashes to the one you’re trying to crack to see if they match. If they do, you know what word corresponds to that hash- you’ve cracked it!

This process is called a **dictionary attack**, and *John the Ripper*, or John as it’s commonly shortened, is a tool for conducting fast brute force attacks on various hash types.

### Setting Up Your System

If you use the attached virtual machine or the AttackBox, you don’t need to install John the Ripper on your system. Consequently, feel free to skip through the installation section. If you prefer to use your system to follow along, please read along to learn how to proceed with the installation. We should note that if you use a version of John the Ripper other than Jumbo John, you might not have some of the required tools, such as `zip2john` and `rar2john`.

#### Installation

John the Ripper is supported on many Operating Systems, not just Linux Distributions. Before we go through this, there are multiple versions of John, the standard “core” distribution, and multiple community editions, which extend the feature set of the original John distribution. The most popular of these distributions is the **“Jumbo John,”** which we will use specific features of later.

##### => Linux 

Many Linux distributions have John the Ripper available for installation from their official repositories. For instance, on Fedora Linux, you can install John the Ripper with `sudo dnf install john`, while on Ubuntu, you can install it with `sudo apt install john. Unfortunately, at the time of writing, these versions provided core functionality and missed some of the tools available through Jumbo John.

Consequently, you need to consider building from the source to access all the tools available via Jumbo John. [Official Installation Guide](https://github.com/openwall/john/blob/bleeding-jumbo/doc/INSTALL) provides detailed installation and build configuration instructions.

##### => Windows

To install Jumbo John the Ripper on Windows, you need to download and install the zipped binary for either 64-bit systems [here](https://www.openwall.com/john/k/john-1.9.0-jumbo-1-win64.zip) or for 32-bit systems [here](https://www.openwall.com/john/k/john-1.9.0-jumbo-1-win32.zip).


#### Wordlists

Now that we have `john` ready, we must consider another indispensable component: **wordlists**.

As we mentioned earlier, to use a dictionary attack against hashes, you need a list of words to hash and compare; unsurprisingly, this is called a wordlist. There are many different wordlists out there, and a good collection can be found in the [SecLists](https://github.com/danielmiessler/SecLists)  repository. There are a few places you can look for wordlists for attacking the system of choice; we will quickly run through where you can find them. 

##### RockYou

you can get the `rockyou.txt` wordlist from the [SecLists](https://github.com/danielmiessler/SecLists) repository under the `/Passwords/Leaked-Databases` subsection. You may need to extract it from the `.tar.gz` format using `tar xvzf rockyou.txt.tar.gz` 

---

## Cracking Basic Hashes

#### John Basic Syntax

The basic syntax of John the Ripper commands is as follows. We will cover the specific options and modifiers used as we use them.

`john [options] [file path]`

- **john**: Invokes the John the Ripper program  
- **[options]**: Specifies the options you want to use  
- **[file path]**: The file containing the hash you’re trying to crack; if it’s in the same directory, you won’t need to name a path, just the file.

#### Automatic Cracking

John has built-in features to detect what type of hash it’s being given and to select appropriate rules and formats to crack it for you; this isn’t always the best idea as it can be unreliable, but if you can’t identify what hash type you’re working with and want to try cracking it, it can be a good option! To do this, we use the following syntax:

`john --wordlist=[path to wordlist] [path to file]`

- **--wordlist=**: Specifies using wordlist mode, reading from the file that you supply in the provided path  
- **[path to wordlist]**: The path to the wordlist you’re using, as described in the previous task  
- **[path to file]**: The file containing the hash you want to crack  

*Example Usage:* `john --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt`

#### Identifying Hashes

Sometimes, John won’t play nicely with automatically recognising and loading hashes, but that’s okay! We can use other tools to identify the hash and then set John to a specific format. There are multiple ways to do this, such as using an online hash identifier like [this site ](https://hashes.com/en/tools/hash_identifier). I like to use a tool called [hash-identifier](https://gitlab.com/kalilinux/packages/hash-identifier/-/tree/kali/master), a Python tool that is super easy to use and will tell you what different types of hashes the one you enter is likely to be, giving you more options if the first one fails.

To use hash-identifier, you can use `wget` or `curl` to download the Python file `hash-id.py` from its GitLab [hash-id.py script](https://gitlab.com/kalilinux/packages/hash-identifier/-/raw/kali/master/hash-id.py). Then, launch it with `python3 hash-id.py` and enter the hash you’re trying to identify. It will give you a list of the most probable formats. These two steps are shown in the terminal below. 

<img src="./Cybersecurity_101_screenshots/john_the_ripper01.jpg" width="800" alt="Screenshot 1"> <br>

#### Format-Specific Cracking

Once you have identified the hash that you’re dealing with, you can tell John the Ripper to use it while cracking the provided hash using the following syntax:

```bash
john --format=[format] --wordlist=[path to wordlist] [path to file]
```
- `--format=`: This is the flag to tell John that you’re giving it a hash of a specific format and to use the following format to crack it
- `[format]`: The format that the hash is in

*Example Usage:* `john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt`

- When you tell John to use formats, if you’re dealing with a standard hash type, e.g. md5 as in the example above, you have to prefix it with `raw-` to tell John you’re just dealing with a standard hash type, though this doesn’t always apply. To check if you need to add the prefix or not, you can list all of John’s formats using `john --list=formats` and either check manually or grep for your hash type using something like `john --list=formats | grep -iF "md5"`.


### Cracking Windows Authentication Hashes

#### NTHash / NTLM

NThash is the hash format modern Windows operating system machines use to store user and service passwords. It’s also commonly referred to as NTLM, which references the previous version of Windows format for hashing passwords known as LM, thus NT/LM.

In Windows, SAM (Security Account Manager) is used to store user account information, including usernames and hashed passwords. You can acquire NTHash/NTLM hashes by dumping the SAM database on a Windows machine, using a tool like **Mimikatz**, or using the Active Directory database: **NTDS.dit**. You may not have to crack the hash to continue privilege escalation, as you can often conduct a “pass the hash” attack instead, but sometimes, hash cracking is a viable option if there is a weak password policy.


### Cracking /etc/shadow Hashes

The `/etc/shadow` file is the file on Linux machines where password hashes are stored. It also stores other information, such as the date of last password change and password expiration information. It contains one entry per line for each user or user account of the system. This file is usually only accessible by the root user, so you must have sufficient privileges to access the hashes. However, if you do, there is a chance that you will be able to crack some of the hashes.

#### Unshadowing
John can be very particular about the formats it needs data in to be able to work with it; for this reason, to crack `/etc/shadow` passwords, you must combine it with the `/etc/passwd` file for John to understand the data it’s being given. To do this, we use a tool built into the John suite of tools called `unshadow`. The basic syntax of `unshadow` is as follows: `unshadow [path to passwd] [path to shadow]`

- `unshadow`: Invokes the unshadow tool
- `[path to passwd]`: The file that contains the copy of the `/etc/passwd` file you’ve taken from the target machine
- `[path to shadow]`: The file that contains the copy of the `/etc/shadow` file you’ve taken from the target machine

*Example Usage:* `unshadow local_passwd local_shadow > unshadowed.txt`

**Note on the files**: When using unshadow, you can either use the entire `/etc/passwd` and `/etc/shadow` files, assuming you have them available, or you can use the relevant line from each, for example:
- **FILE 1 - local_passwd:** Contains the `/etc/passwd` line for the root user:`root:x:0:0::/root:/bin/bash`
- **FILE 2 - local_shadow**: Contains the `/etc/shadow` line for the root user: `root:$6$2nwjN454g.dv4HN/$m9Z/r2xVfweYVkrr.v5Ft8Ws3/YYksfNwq96UL1FX0OJjY1L6l.DS3KEVsZ9rOVLB/ldTeEL/OIhJZ4GMFMGA0:18576::::::`
  
#### Cracking

We can then feed the output from `unshadow`, in our example use case called `unshadowed`.txt, directly into John. We should not need to specify a mode here as we have made the input specifically for John; however, in some cases, you will need to specify the format as we have done previously using: `--format=sha512crypt john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt`

### Single Crack Mode

So far, we’ve been using John’s wordlist mode to brute-force simple and not-so-simple hashes. But John also has another mode, called the Single Crack mode. In this mode, John uses only the information provided in the username to try and work out possible passwords heuristically by slightly changing the letters and numbers contained within the username.

#### Word Mangling

The best way to explain Single Crack mode and word mangling is to go through an example:

Consider the username “Markus”.

Some possible passwords could be:

- Markus1, Markus2, Markus3 (etc.)
- MArkus, MARkus, MARKus (etc.)
- Markus!, Markus$, Markus* (etc.)

This technique is called word mangling. John is building its dictionary based on the information it has been fed and uses a set of rules called “mangling rules,” which define how it can mutate the word it started with to generate a wordlist based on relevant factors for the target you’re trying to crack. This exploits how poor passwords can be based on information about the username or the service they’re logging into.

#### GECOS

John’s implementation of word mangling also features compatibility with the GECOS field of the UNIX operating system, as well as other UNIX-like operating systems such as Linux. GECOS stands for General Electric Comprehensive Operating System. In the last task, we looked at the entries for both `/etc/shadow` and `/etc/passwd`. Looking closely, you will notice that the fields are separated by a colon `:`. The fifth field in the user account record is the GECOS field. It stores general information about the user, such as the user’s full name, office number, and telephone number, among other things. John can take information stored in those records, such as full name and home directory name, to add to the wordlist it generates when cracking `/etc/shadow` hashes with single crack mode.

#### Using Single Crack Mode

To use single crack mode, we use roughly the same syntax that we’ve used so far; for example, if we wanted to crack the password of the user named “Mike”, using the single mode, we’d use: `john --single --format=[format] [path to file]`
- `--single`: This flag lets John know you want to use the single hash-cracking mode.
- `--format=[format]`: As always, it is vital to identify the proper format.

*Example Usage:* `john --single --format=raw-sha256 hashes.txt`

**A Note on File Formats in Single Crack Mode:** If you’re cracking hashes in single crack mode, you need to change the file format that you’re feeding John for it to understand what data to create a wordlist from. You do this by prepending the hash with the username that the hash belongs to, so according to the above example, we would change the file `hashes.txt`
- **From** `1efee03cdcb96d90ad48ccc7b8666033` **To** `mike:1efee03cdcb96d90ad48ccc7b8666033`

---

## Custom Rules


As we explored what John can do in Single Crack Mode, you may have some ideas about some good mangling patterns or what patterns your passwords often use that could be replicated with a particular mangling pattern. The good news is that you can define your rules, which John will use to create passwords dynamically. The ability to define such rules is beneficial when you know more information about the password structure of whatever your target is.

#### Common Custom Rules

Many organisations will require a certain level of password complexity to try and combat dictionary attacks. In other words, when creating a new account or changing your password, if you attempt a password like `polopassword`, it will most likely not work. The reason would be the enforced password complexity. As a result, you may receive a prompt telling you that passwords have to contain at least one character from each of the following:

- Lowercase letter  
- Uppercase letter  
- Number  
- Symbol  

Password complexity is good! However, we can exploit the fact that most users will be predictable in the location of these symbols. For the above criteria, many users will use something like the following:

**Example pattern:** ```Polopassword1!```

Consider the password with a capital letter first and a number followed by a symbol at the end. This familiar pattern of the password, appended and prepended by modifiers (such as capital letters or symbols), is a memorable pattern that people use and reuse when creating passwords. This pattern can let us exploit password complexity predictability.

Now, this does meet the password complexity requirements; however, as attackers, we can exploit the fact that we know the likely position of these added elements to create dynamic passwords from our wordlists.

## How to Create Custom Rules

Custom rules are defined in the `john.conf` file. This file can typically be found in:

- `/opt/john/john.conf`  
- `/etc/john/john.conf` (if installed using a package manager or built from source with `make`)

Let’s go over the syntax of these custom rules using the example pattern mentioned earlier as our target. You can define a massive level of granular control in these rules.

Refer to the official John the Ripper documentation for full details on modifiers and additional examples:  
[https://www.openwall.com/john/doc/RULES.shtml](https://www.openwall.com/john/doc/RULES.shtml)

The first line: ```[List.Rules:THMRules] ```
is used to define the name of your rule. This is what you will use to call your custom rule as a John argument.

We then use a regex-style pattern match to define where the word will be modified. Below are some of the primary and most common modifiers:

| Modifier | Description |
|----------|-------------|
| `Az`     | Appends characters to the end of the word |
| `A0`     | Prepends characters to the beginning of the word |
| `c`      | Capitalises the character positionally |

These modifiers can be combined to define where and what in the word you want to modify.

Character sets are added using square brackets `[ ]` and placed within double quotes `" "` after the modifiers. Some common sets include:

| Character Set | Description |
|---------------|-------------|
| `[0-9]`        | Includes numbers 0 through 9 |
| `[0]`          | Includes only the number 0 |
| `[A-z]`        | Includes both uppercase and lowercase letters |
| `[A-Z]`        | Includes only uppercase letters |
| `[a-z]`        | Includes only lowercase letters |
| `[a]`          | Includes only the letter "a" |
| `[!£$%@]`      | Includes specified symbols: `!`, `£`, `$`, `%`, `@` |

### Example Custom Rule

To match the password pattern `Polopassword1!` (assuming `polopassword` exists in the wordlist), a custom rule entry could look like this:

```
[List.Rules:PoloPassword]
cAz"[0-9][!£$%@]"
```

This rule does the following:

- `c`: Capitalises the first letter  
- `Az`: Appends to the end of the word  
- `[0-9]`: Appends a digit between 0–9  
- `[!£$%@]`: Appends one of the specified symbols

### Using Custom Rules

You can call this custom rule with the `--rule` flag: ``` john --wordlist=[path to wordlist] --rule=PoloPassword [path to file] ```

> It can be helpful to talk through the patterns as you write a rule, similar to how you might approach writing a regular expression.

Jumbo John includes an extensive list of preconfigured rules. If you're having trouble with your syntax, check the rules starting around line 678 in `john.conf` for reference and working examples.


### Cracking Password Protected Zip Files

John can crack passwords on password-protected Zip files using the `zip2john` tool to convert the file into a hash format John understands.

#### Zip2John
Converts a Zip file into a hash format for John. Basic syntax:
`zip2john [options] [zip file] > [output file]`

- `[options]`: Optional checksum settings (rarely needed)  
- `[zip file]`: Path to the target Zip file  
- `>`: Redirects output to a file  
- `[output file]`: Stores the extracted hash  

**Example usage:**   `zip2john zipfile.zip > zip_hash.txt`

#### Cracking the Hash
Feed the output file (`zip_hash.txt`) directly into John with a wordlist:  
`john --wordlist=/usr/share/wordlists/rockyou.txt zip_hash.txt`



### Cracking Password-Protected RAR Archives

#### Rar2John

Almost identical to the `zip2john` tool, we will use the `rar2john` tool to convert the RAR file into a hash format that John can understand. The basic syntax is as follows:`rar2john [rar file] > [output file]`

- `rar2john`: Invokes the `rar2john` tool
- `[rar file]`: The path to the RAR file you wish to get the hash of
- `>`: This redirects the output of this command to another file
- `[output file]`: This is the file that will store the output from the command

*Example Usage:* `/opt/john/rar2john rarfile.rar > rar_hash.txt`

#### Cracking

Once again, we can take the file we output from `rar2john` in our example use case, `rar_hash.txt`, and feed it directly into John as we did with `zip2john`.

`john --wordlist=/usr/share/wordlists/rockyou.txt rar_hash.txt`


### Cracking SSH Keys with John

#### Cracking SSH Key Passwords

Okay, okay, I hear you. There are no more file archives! Fine! Let’s explore one more use of John that comes up semi-frequently in CTF challenges—using John to crack the SSH private key password of `id_rsa` files. Unless configured otherwise, you authenticate your SSH login using a password. However, you can configure key-based authentication, which lets you use your private key, `id_rsa`, as an authentication key to log in to a remote machine over SSH. However, doing so will often require a password to access the private key; here, we will be using John to crack this password to allow authentication over SSH using the key.

#### SSH2John

Who could have guessed it, another conversion tool? Well, that’s what working with John is all about. As the name suggests, `ssh2john` converts the `id_rsa` private key, which is used to log in to the SSH session, into a hash format that John can work with. Jokes aside, it’s another beautiful example of John’s versatility. The syntax is about what you’d expect. Note that if you don’t have `ssh2john` installed, you can use `ssh2john.py`, located in the `/opt/john/ssh2john.py`. If you’re doing this on the AttackBox, replace the `ssh2john` command with `python3 /opt/john/ssh2john.py` or on Kali, `python /usr/share/john/ssh2john.py`.

`ssh2john [id_rsa private key file] > [output file]`

- `ssh2john`: Invokes the `ssh2john` tool
- `[id_rsa private key file]`: The path to the id_rsa file you wish to get the hash of
- `>`: This is the output director. We’re using it to redirect the output from this command to another file.
- `[output file]`: This is the file that will store the output from


*Example Usage:* `/opt/john/ssh2john.py id_rsa > id_rsa_hash.txt`

#### Cracking

For the final time, we’re feeding the file we output from ssh2john, which in our example use case is called `id_rsa_hash.txt` and, as we did with `rar2john`, we can use this seamlessly with John: `john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt`

---
> **Note:** These notes document hands-on learning from the TryHackMe *Cybersecurity 101* path. The exercises cover fundamental cybersecurity topics, including Linux basics, networking concepts, and web technologies. This document is intended for personal learning, revision, and ethical skill development. All screenshots, commands, and actions are for educational purposes only.  
> — Compiled by moh4med404 | Curious Mind | Cybersecurity Enthusiast