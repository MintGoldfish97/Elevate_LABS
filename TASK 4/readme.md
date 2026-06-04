# Task 4 - Setup and Use a Firewall on Windows/Linux

## Objective

Configure and test basic firewall rules to allow or block network traffic and understand how firewalls filter network communications.

---

## Tools Used

* Windows Defender Firewall
* Ubuntu Linux
* UFW (Uncomplicated Firewall)
* OpenSSH Server
* Telnet Client
* Python HTTP Server

---

## Environment

### Windows Host

* Windows Defender Firewall
* Python HTTP Server running on Port 23

### Ubuntu Machine

* UFW Firewall
* OpenSSH Server
* Telnet Client

---

## Task Performed

### 1. Blocking Telnet Port 23 on Windows Firewall

A new inbound firewall rule was created in Windows Defender Firewall to block TCP Port 23 (Telnet).

Purpose:

* Prevent incoming Telnet connections.
* Demonstrate traffic filtering using firewall rules.

---

### 2. Testing the Block Rule

To test the firewall rule, a Python HTTP server was started on Windows using Port 23:

python -m http.server 23
From the Ubuntu machine, a Telnet connection was attempted to the Windows machine:

telnet <windows-ip> 23
Result:

Trying <windows-ip>...
Connection refused
This confirmed that the Windows Firewall rule successfully blocked inbound traffic on Port 23.

---

### 3. Configuring SSH on Ubuntu

The OpenSSH Server was installed and verified on Ubuntu.

Checking SSH service status:

sudo systemctl status ssh
Verifying SSH was listening on Port 22:

sudo ss -tulnp | grep :22
---

### 4. Allowing SSH Through UFW

SSH access was allowed through the Ubuntu firewall:

sudo ufw allow 22/tcp
Verifying firewall rules:

sudo ufw status
Result:

22/tcp ALLOW Anywhere
---

### 5. Testing SSH Connectivity

From Windows Command Prompt, an SSH connection was initiated to the Ubuntu machine:

ssh username@192.168.122.236 -p 22
After entering the correct password, the connection was established successfully.

Result:

Successfully connected to Ubuntu via SSH.
This confirmed that:

* SSH service was running.
* Port 22 was accessible.
* UFW firewall rule was functioning correctly.

---

## Screenshots Included

1. Windows Firewall rule blocking Port 23.
2. Python HTTP Server running on Port 23.
3. Telnet connection refused from Ubuntu.
4. UFW status showing SSH allowed.
5. SSH service status on Ubuntu.
6. Successful SSH login from Windows.

---

## Interview Questions

### What is a Firewall?

A firewall is a security device or software that monitors and filters incoming and outgoing network traffic based on predefined security rules.

### Difference Between Stateful and Stateless Firewall?

* Stateful Firewall: Tracks active connections and makes decisions based on connection state.
* Stateless Firewall: Examines each packet independently without tracking connection state.

### What are Inbound and Outbound Rules?

* Inbound Rules control incoming traffic.
* Outbound Rules control outgoing traffic.

### How Does UFW Simplify Firewall Management?

UFW provides an easy-to-use interface for managing Linux firewall rules without directly configuring iptables.

### Why Block Port 23 (Telnet)?

Telnet sends data, including usernames and passwords, in plain text, making it insecure.

### Common Firewall Mistakes

* Leaving unnecessary ports open.
* Misconfigured rules.
* Allowing unrestricted access.
* Not regularly reviewing firewall policies.

### How Does a Firewall Improve Security?

A firewall blocks unauthorized access, reduces attack surface, and controls network traffic.

### What is NAT in Firewalls?

Network Address Translation (NAT) allows multiple devices on a private network to share a single public IP address.

---

## Outcome

Successfully configured and tested firewall rules on Windows and Linux. Verified that blocked ports prevent unauthorized access and allowed ports permit legitimate services such as SSH. Gained practical experience in firewall management, network traffic filtering, and secure remote access.
