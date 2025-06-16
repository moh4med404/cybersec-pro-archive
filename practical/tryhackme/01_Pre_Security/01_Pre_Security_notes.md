# Pre-Security 
---
# Offensive and Defensive Security Intro
### Offensive Security 

Offensive Security refers to proactive security practices where individuals or teams simulate attacks on systems, networks, or applications to identify vulnerabilities before malicious actors can exploit them. It focuses on offensive techniques, essentially "hacking back" in a controlled, ethical manner to help organizations strengthen their defenses. Example: 

<img src="./pre-security-screenshots/screenshot01.jpg" width="800"  alt="Screenshot 1">

**Explanation**:  

```bash
gobuster -u http://fakebank.thm -w wordlist.txt dir
```

is used for **directory brute-forcing** on the website `http://fakebank.thm` using a wordlist (`wordlist.txt`). Here's how it works:

1. **`-u` (URL)**: Specifies the target website to scan (`http://fakebank.thm`).
2. **`-w` (Wordlist)**: Defines the wordlist (`wordlist.txt`) that contains potential directory names (like `admin`, `login`, etc.).
3. **`dir`**: Instructs Gobuster to scan for **directories** on the target website.

Gobuster will try each word from the wordlist as a directory path (e.g., `http://fakebank.thm/admin`) and check the server's response. If it finds a valid directory, it will report it along with the HTTP response code (e.g., `200 OK`).

This helps to discover hidden directories on a web server that might not be visible through regular browsing, which could be useful for penetration testing or bug bounty hunting. now we found hidden page /bank-transfer. 


<img src="./pre-security-screenshots/screenshot02.jpg" width="800" alt="Screenshot 2">
<img src="./pre-security-screenshots/screenshot03.jpg" width="800" alt="Screenshot 3">

**Explanation**:  
##### After discovering the hidden /bank-transfer page, we gained access and successfully transferred $2000 from account 2276 to our account (8881)

### Defensive Security 

Defensive Security (also known as Blue Teaming) focuses on protecting systems, networks, and data from potential threats by implementing security measures to prevent attacks. Unlike Offensive Security, which involves actively trying to exploit vulnerabilities, defensive security works on identifying, mitigating, and responding to threats to secure an organization's infrastructure. Example: Let's say, as part of your daily work, you open your SIEM dashboard to review the logs and notice unauthorized access logs 

<img src="./pre-security-screenshots/screenshot04.jpg" width="800" alt="Screenshot 4">
<img src="./pre-security-screenshots/screenshot05.jpg" width="800" alt="Screenshot 5">

In this step, I performed a scan to investigate the suspicious IP address identified in the SIEM logs. This scan helps us gather more information about the potential threat, such as its origin, behavior, and any associated malicious activity.

<img src="./pre-security-screenshots/screenshot06.jpg" width="800" alt="Screenshot 6">

After confirming the malicious nature of the IP address, I proceeded to block it at the firewall level. This step prevents further communication from the compromised IP, mitigating the risk of an ongoing attack or data breach

<img src="./pre-security-screenshots/screenshot07.jpg" width="800"  alt="Screenshot 7">

---
# Networking
---

Networking is the process of connecting with people or devices to share information, resources, or opportunities. In a professional sense, it’s about building relationships to help advance your career or business. In technology, it’s about linking devices to share data and resources.

<img src="./pre-security-screenshots/screenshot08.jpg" width="800"  alt="Screenshot 8">

Devices on a network are very similar to humans in the fact that we have two ways of being identified:

- Our Name
- Our Fingerprints

Now we can change our name through deed poll, but we can't, however, change our fingerprints. Every human has an individual set of fingerprints which means that even if they change their name, there is still an identity behind it. Devices have the same thing: two means of identification, with one being permeable. These are:

- An IP Address
- A Media Access Control (MAC) Address -- think of this as being similar to a serial number. 

Devices within a local network will have different private IPs to communicate with each other, but they will share the same public IP when communicating with the outside world. This is typically managed through a process called **NAT (Network Address Translation)**. 

A **Public IP** is an address accessible over the internet, unique across the web. A **Private IP** is used within local networks and isn’t visible on the internet. A **MAC Address** is a unique identifier assigned to a device’s network interface, used for local network communication.

<img src="./pre-security-screenshots/screenshot09.jpg" width="800"  alt="Screenshot 9">

Every device on a network has a physical network interface, which is a small chip located on the device’s motherboard. This interface is given a unique identifier called a MAC (Media Access Control) address during manufacturing. The MAC address is made up of twelve hexadecimal characters (numbers and letters from 0–9 and A–F), grouped in pairs and separated by colons, like this: a4:c3:f0:85:ac:2d. The first half of the address identifies the manufacturer of the network interface, while the second half is a unique code assigned to that specific device.

<img src="./pre-security-screenshots/screenshot10.jpg" width="800"  alt="Screenshot 10">

### Ping 

**Ping** is a basic network tool that helps check if two devices can communicate with each other. It works by sending special messages called ICMP packets to a target device and waiting for a response. The tool measures how long it takes for these messages to travel back and forth, showing if the connection is working and how fast it is.

You can use ping to test devices on your local network or websites on the internet. It’s easy to use and is already installed on most operating systems like Windows and Linux. To use it, you simply type ping followed by an IP address or website name.

<img src="./pre-security-screenshots/screenshot11.jpg" width="800"  alt="Screenshot 11">
<img src="./pre-security-screenshots/screenshot12.jpg" width="800"  alt="Screenshot 12">

### Netcat (nc) 

**Netcat** is a command-line networking tool used to read from and write to network connections using TCP or UDP protocols. It is often referred to as the "Swiss Army knife" of networking because it can perform many functions, such as testing connectivity, transferring files, scanning ports, and creating simple servers or clients. Netcat is often used for:
- Checking if a port is open on a remote host.
- Sending or receiving data over a network.
- Debugging network services.

<img src="./pre-security-screenshots/screenshot13.jpg" width="800"  alt="Screenshot 13">

**Explanation**:  

```bash
nc 8.8.8.8 1234
```
- **nc:** Short for Netcat, a command-line networking tool.
- **8.8.8.8:** The target IP address (Google's public DNS server in this case).
- **1234:** The target port number you're trying to connect to.

### Firewall 

**A firewall** is a network security device or software that monitors and controls incoming and outgoing traffic based on predetermined rules. Its main purpose is to act as a barrier between a trusted internal network and untrusted external networks, such as the internet. Firewalls can prevent unauthorized access, block harmful traffic, and enforce security policies by filtering data based on IP addresses, ports, protocols, and even application-level content. They come in various types—such as packet-filtering, stateful inspection, proxy, and next-generation firewalls—and are essential for protecting systems from cyber threats and maintaining network integrity.
### 🔐 Example Firewall Rules

- **Allow** incoming HTTP (port 80) and HTTPS (port 443) traffic  
- **Block** all incoming traffic from blacklisted IP addresses  
- **Deny** access to port 23 (Telnet) to prevent unencrypted remote logins  
- **Allow** internal devices to access the DNS server on port 53  
- **Block** outbound traffic to known malware domains


<img src="./pre-security-screenshots/screenrec01.gif" width="800"  alt="screenrec 1">

### How Data Moves Through a Network

In this task, I'm using a network simulator to observe how data moves through a network. The simulator clearly shows each step a packet takes as it travels from one device to another. I’ll be sending a TCP packet from Computer1 to Computer3 to follow the full process and understand how the connection is established.

<img src="./pre-security-screenshots/screenrec02.gif" width="800"  alt="screenrec 2">

### 🖧 TCP/IP Network Log

**HANDSHAKE:** Starting TCP/IP handshake between Computer1 and Computer3  
**HANDSHAKE:** Sending SYN packet from Computer1 to Computer3  

**ROUTING:**  
- Computer1 says Computer3 is not on the local network  
- Sending packet to the gateway: Router  

**ARP REQUEST:** Who has Router? Tell Computer1  
**ARP RESPONSE:** Hey Computer1, I am Router  

**ARP REQUEST:** Who has Computer3? Tell Router  
**ARP RESPONSE:** Hey Router, I am Computer3  

**HANDSHAKE:**  
- Computer3 received SYN packet from Computer1  
- Sending SYN/ACK packet to Computer1  
- Computer1 received SYN/ACK packet from Computer3  
- Sending ACK packet to Computer3  
- Computer3 received ACK — *Handshake complete*  

**TCP:**  
- Sending TCP packet from Computer1 to Computer3  
- Computer3 received TCP packet, sending ACK to Computer1  

## DNS
**DNS (Domain Name System)** is like the internet’s phonebook, making it easy for us to connect with websites without having to memorize complicated numbers. Just like every home has a unique mailing address, every device on the internet has a unique numerical label called an IP address, such as 104.26.10.229 — a series of four numbers between 0 and 255 separated by dots. Since remembering these numbers for every site would be tough, DNS lets us use simple names like tryhackme.com instead, which then get translated behind the scenes to the corresponding IP address.

**Domain Hierarchy**
<img src="./pre-security-screenshots/screenshot14.gif" width="800"  alt="Screenshot 14">

### 🧠 DNS Enumeration with `nslookup`

As part of my TryHackMe journey, I practiced basic DNS enumeration using the `nslookup` command. The goal was to extract different types of DNS records to uncover hidden data and understand how domain resolution works.

#### 🔁 CNAME Record Lookup

I began by checking for a **CNAME record** using:

```bash
nslookup --type=CNAME shop.website.thm
```

📌 This tells us that `shop.website.thm` is an alias for `shops.myshopify.com`, which means DNS queries are redirected to that domain — a common setup for external service integrations.

#### 🧾 TXT Record Lookup

Next, I checked for **TXT records**, which can include verification text or flags:

```bash
nslookup --type=TXT website.thm
```

🎯 I found a hidden flag in the TXT record:  
`THM{7012BBA60997F35A9516C2E16D2944FF}`  
This is likely part of the room's challenge.


#### 🌐 A Record Lookup

Finally, I ran a basic DNS query to get the IP address (A record) of the domain:

```bash
nslookup website.thm
```
<img src="./pre-security-screenshots/screenshot15.jpg" width="800"  alt="Screenshot 15">

## HTTP vs HTTPS

- **HTTP (HyperText Transfer Protocol):**  
  A protocol for transferring data over the web. Data is sent **unencrypted**, which can be intercepted.

- **HTTPS (HTTP Secure):**  
  HTTP with **encryption (TLS/SSL)** to secure data between client and server, protecting privacy and integrity.

### Common HTTP Methods

| Method | Purpose                        |
|--------|-------------------------------|
| GET    | Retrieve data from a server    |
| POST   | Send data to create a resource |
| PUT    | Update an existing resource    |
| DELETE | Remove a resource              |
| PATCH  | Partially update a resource    |
| HEAD   | Get headers only (no body)     |

Using HTTPS with proper HTTP methods ensures secure and efficient communication on the web.

### HTTP Status Codes 

When a web server replies to a client's request, the first line of the response includes a **status code**. This code tells the client whether their request succeeded, failed, or if further action is needed. Status codes are grouped into five categories based on their number range:

- **100-199: Informational Responses**  
  These codes indicate the server has received part of the request and the client should continue sending the rest. They are rarely used nowadays.

- **200-299: Success**  
  Codes in this range mean the client’s request was successfully received and processed.

- **300-399: Redirection**  
  These codes tell the client to look somewhere else for the requested resource. This could be a new webpage or a completely different website.

- **400-499: Client Errors**  
  These indicate something was wrong with the client’s request, such as missing data or unauthorized access.

- **500-599: Server Errors**  
  These codes show that the server encountered an issue while trying to fulfill the request, often indicating a serious problem on the server side.

### Common HTTP Status Codes

While there are many HTTP status codes (and some apps even create their own), here are some you’ll frequently see:

| Code | Meaning               | Description                                                                                  |
|-------|----------------------|----------------------------------------------------------------------------------------------|
| 200   | OK                   | The request was successfully completed.                                                     |
| 201   | Created              | A new resource was successfully created, like a user account or a blog post.                 |
| 301   | Moved Permanently    | Redirects the client permanently to a new URL; search engines update their links accordingly.|
| 302   | Found (Temporary Redirect) | Redirects the client temporarily; the location might change again soon.                   |
| 400   | Bad Request          | The request was malformed or missing important information.                                  |
| 401   | Unauthorized         | Access denied because the client is not authenticated (usually requires login).              |
| 403   | Forbidden            | The client does not have permission to access this resource, regardless of authentication.  |
| 404   | Not Found            | The requested page or resource does not exist on the server.                                 |
| 405   | Method Not Allowed   | The HTTP method used (GET, POST, etc.) is not supported for the requested resource.          |
| 500   | Internal Server Error | The server encountered an unexpected problem and could not process the request.             |
| 503   | Service Unavailable  | The server is currently unable to handle the request, often due to overload or maintenance.  |

Understanding these codes helps when troubleshooting websites or building web applications, as they give insight into how requests are handled and where problems might occur.

**403 Error**
<img src="./pre-security-screenshots/screenshot16.jpg" width="800"  alt="Screenshot 16"> 

**404 Error**
<img src="./pre-security-screenshots/screenshot17.jpg" width="800"  alt="Screenshot 17">

**503 Error**
<img src="./pre-security-screenshots/screenshot18.jpg" width="800"  alt="Screenshot 18">

## Introduction to Cookies

Cookies are small pieces of data that websites store on your browser.  
They help websites remember your preferences, keep you logged in, and track your activity.  

Cookies are sent back and forth between your browser and the web server with each request,  
making them important for managing sessions and personalized experiences.  

However, cookies can also be a target for security testing since they may contain sensitive information like session tokens.

### Why Use Developer Tools?

Developer Tools (DevTools) are built into web browsers to help developers and security enthusiasts:

- **Inspect** the HTML, CSS, and JavaScript of a webpage.
- **Debug** issues with webpage layout, scripts, or network requests.
- **Monitor** network traffic to see what data is being sent and received.
- **Test** changes live without modifying the original website.
- **Analyze** security-related information, such as cookies and headers.

In cybersecurity challenges like TryHackMe, DevTools help explore and understand how websites work, find hidden data, or inspect vulnerabilities.

### Accessing Developer Tools

#### Firefox
- Click the **Firefox Menu** icon (top right).  
- Select **More tools**.  
- Choose **Web Developer Tools**.

#### Chrome
- Click the **three dots** menu (top right).  
- Go to **More tools** → **Developer tools**.  
- Or press `Ctrl + Shift + I` (Windows/Linux) or `Cmd + Option + I` (Mac).

#### Safari
- Enable the **Develop** menu first via Preferences → Advanced → Check **Show Develop menu in menu bar**.  
- Then select **Develop** → **Show Web Inspector**.  
- Or press `Cmd + Option + I`.

#### Edge
- Click the **three dots** menu (top right).  
- Go to **More tools** → **Developer tools**.  
- Or press `F12` or `Ctrl + Shift + I`.

#### Internet Explorer
- Press `F12`.  
- Or click the **gear icon** → **F12 Developer Tools**.

<br><br>
> **Note:** These notes document hands-on learning from the TryHackMe *Pre-Security* path. The exercises cover fundamental cybersecurity topics, including Linux basics, networking concepts, and web technologies. This document is intended for personal learning, revision, and ethical skill development. All screenshots, commands, and actions are for educational purposes only.  
> — Compiled by moh4med404 | Curious Mind | Cybersecurity Enthusiast