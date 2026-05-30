You can use the following README.md content for your GitHub repository:

# Task 1 – Scan Your Local Network for Open Ports

## Objective

The objective of this task is to learn basic network reconnaissance techniques by identifying active hosts and open ports on a local network using Nmap. This helps in understanding network exposure and potential security risks associated with exposed services.

## Tools Used

* Nmap
* Kali Linux
* Wireshark (Optional)
* GitHub

## Network Information

* IP Address: 10.0.2.15
* Subnet Mask: 255.255.255.0
* Network Range: 10.0.2.0/24

## Procedure

### 1. Identify Network Range

The network configuration was identified using the following command:

```bash
ifconfig
```

The system was assigned the IP address `10.0.2.15` with a subnet mask of `255.255.255.0`, resulting in a network range of `10.0.2.0/24`.

### 2. Perform Host Discovery

A ping scan was conducted to identify active hosts on the network:

```bash
nmap -sn 10.0.2.0/24
```

### 3. Perform TCP SYN Scan

A TCP SYN scan was executed against the local network:

```bash
sudo nmap -sS 10.0.2.0/24
```

The scan identified an active host at `10.0.2.3` with multiple open TCP ports.

### 4. Analyze Open Ports

The following open ports were discovered:

| Port | Service           |
| ---- | ----------------- |
| 21   | FTP               |
| 22   | SSH               |
| 23   | Telnet            |
| 25   | SMTP              |
| 53   | DNS               |
| 80   | HTTP              |
| 111  | RPCBind           |
| 139  | NetBIOS           |
| 445  | SMB               |
| 512  | rexec             |
| 513  | rlogin            |
| 514  | rsh               |
| 1099 | Java RMI Registry |
| 1524 | ingreslock        |
| 2049 | NFS               |
| 2121 | FTP Proxy         |
| 3306 | MySQL             |
| 5432 | PostgreSQL        |
| 5900 | VNC               |
| 6000 | X11               |
| 6667 | IRC               |
| 8009 | AJP13             |
| 8180 | HTTP Service      |

## Potential Security Risks

Several exposed services could increase the attack surface of the host:

* Telnet (23) transmits data in plaintext and is considered insecure.
* SMB (445) may expose file-sharing services to unauthorized access.
* FTP (21) can expose credentials if encryption is not used.
* VNC (5900) allows remote desktop access and may be vulnerable to weak authentication.
* MySQL (3306) and PostgreSQL (5432) databases could be exposed if improperly configured.
* Legacy services such as rlogin, rsh, and rexec are considered insecure and should be disabled when not required.
* Web services running on ports 80, 8009, and 8180 may be susceptible to web application vulnerabilities if not maintained.

## Wireshark Analysis

Wireshark was used to observe network packets generated during the Nmap scan. TCP SYN packets, SYN-ACK responses, and RST packets were analyzed to understand how a TCP SYN scan identifies open ports without completing the TCP three-way handshake.

Useful Wireshark filter:

```text
ip.addr == 10.0.2.15 && ip.addr == 10.0.2.3
```

## Findings

* One active host was identified on the network.
* A total of 23 TCP ports were found open.
* Multiple services related to remote access, file sharing, databases, and web applications were exposed.
* The host presented a large attack surface due to the number of running services.

## Conclusion

This task provided hands-on experience with network reconnaissance using Nmap. Open ports and exposed services were identified, and their potential security implications were analyzed. The exercise demonstrated the importance of port scanning as an initial step in network security assessments and vulnerability management.
