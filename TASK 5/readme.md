# 🔬 Network Traffic Analysis — Wireshark Packet Capture

> **Task 5 | Cyber Security Internship — Elevate Labs**  
> Capture and analyze live network traffic using Wireshark, identify protocols, and document findings.

---

## 📋 Objective

Capture live network packets using Wireshark and identify key protocols and traffic patterns from a real network environment.

---

## 📊 Capture Summary

| Metric | Value |
|--------|-------|
| Total Packets Captured | 5,364 |
| Capture Duration | ~103 seconds |
| Capture Interface | Ethernet (Network Type 1) |
| Local Machine IP | 192.168.231.35 |

---

### 1. 🔵 TCP — Transmission Control Protocol

**Wireshark Filter:** `tcp`  
**Packet Count:** 4,073

**What it is:**  
TCP is a connection-oriented transport layer protocol that ensures reliable, ordered delivery of data between two hosts. It uses a three-way handshake (SYN → SYN-ACK → ACK) to establish a connection before any data is sent.

**Observed in capture:**  
- TCP was the dominant protocol, carrying the majority of all traffic.
- Used as the underlying transport for both HTTP and HTTPS/TLS sessions.
- TCP connections were observed to/from Google servers (`142.251.156.119`) and Microsoft servers (`20.190.146.34`).

**Key characteristics:**
- Connection-oriented (requires handshake)
- Guarantees delivery and ordering
- Uses acknowledgment (ACK) and retransmission
- Ports: 80 (HTTP), 443 (HTTPS)

---

### 2. 🟢 TLS — Transport Layer Security (HTTPS)

**Wireshark Filter:** `tls`  
**Packet Count:** 3,311

**What it is:**  
TLS is a cryptographic protocol that provides encrypted communication over TCP. It is the "S" in HTTPS. TLS operates above TCP and encrypts the application data so it cannot be read by anyone intercepting the traffic.

**Observed in capture:**  
- TLS was the most common application-layer protocol, accounting for over 61% of all packets.
- TLS handshakes (ClientHello, ServerHello, Certificate) were observed at the start of HTTPS sessions.
- Destinations included Google, Microsoft, and blueteamlabs.online.
- Wireshark shows TLS records but **cannot decrypt the payload** without the private key.

**Key characteristics:**
- Runs over TCP port 443
- Uses asymmetric encryption for handshake, symmetric for data
- Provides: confidentiality, integrity, authentication
- Versions seen: TLS 1.2 / TLS 1.3

---

### 3. 🟡 DNS — Domain Name System

**Wireshark Filter:** `dns`  
**Packet Count:** 120

**What it is:**  
DNS translates human-readable domain names (e.g., `google.com`) into IP addresses that computers use to communicate. DNS typically runs over UDP on port 53.

**Observed in capture:**  
DNS queries and responses were captured for the following domains:

| Domain | Query Count |
|--------|------------|
| settings-win.data.microsoft.com | 20 |
| watson.events.data.microsoft.com | 10 |
| google.com | 6 |
| ocsp.digicert.com | 5 |
| play.google.com | 3 |
| fonts.gstatic.com | 3 |
| android.clients.google.com | 3 |
| ecs.office.com | 3 |

**Key characteristics:**
- Runs over UDP port 53 (sometimes TCP for large responses)
- Query types: A (IPv4), AAAA (IPv6), CNAME (alias)
- Each DNS query is followed by a DNS response with the resolved IP

**Observation:**  
Microsoft telemetry domains had the highest DNS query volume, indicating background Windows services were actively communicating during the capture period.

---

### 4. 🟠 QUIC — Quick UDP Internet Connections

**Wireshark Filter:** `quic`  
**Packet Count:** 1,165

**What it is:**  
QUIC is a modern transport protocol developed by Google, built on top of UDP instead of TCP. It is designed to reduce latency and improve performance for web traffic. QUIC is the underlying protocol for HTTP/3.

**Observed in capture:**  
- 1,165 QUIC packets were captured, mainly to/from Google servers (`142.251.156.119`).
- QUIC traffic runs over **UDP port 443**, which is why it appears alongside HTTPS traffic.
- Chrome and other Google services use QUIC by default for faster page loads.

**Key characteristics:**
- Runs over UDP (not TCP)
- Built-in TLS 1.3 encryption
- Reduces connection setup time (0-RTT or 1-RTT vs TCP's 3-way handshake)
- Handles packet loss more efficiently than TCP
- Used by HTTP/3, YouTube, Google Search

**Why QUIC instead of TCP+TLS?**  
TCP requires a handshake before TLS can start — that's 2 round trips minimum. QUIC combines transport and encryption setup into 1 round trip, making connections faster.

---

## 🔎 Wireshark Filters Used

```
dns              → Show all DNS queries and responses
tcp              → Show all TCP packets
tls              → Show all TLS/HTTPS encrypted traffic
quic             → Show all QUIC protocol packets