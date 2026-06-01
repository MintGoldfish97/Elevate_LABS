# Task 2: Phishing Email Sample Analysis
 
## 🎯 Objective
Identify and document phishing characteristics in a suspicious email sample using free online tools.
 
---
 
## 🛠 Tools Used
| Tool | Purpose |
|------|---------|
| [MXToolbox Email Header Analyzer](https://mxtoolbox.com/EmailHeaders.aspx) | Analyze email headers for authentication failures |
| [EML Analyzer](https://eml-analyzer.herokuapp.com/) | Analyze .eml file, extract hops, check OLE attachments |
| [VirusTotal](https://www.virustotal.com/) | Check IP reputation and URL maliciousness |
| [Simple Email Reputation](https://emailrep.io/) | Check sender email reputation |
| [Phishing Pot (GitHub)](https://github.com/rf-peixoto/phishing_pot) | Source of phishing email samples |
 
---
 
## 📧 Sample Email Details
 
| Field | Details |
|-------|---------|
| **Subject** | CLIENTE PRIME - BRADESCO LIVELO: Seu cartão tem 92.990 pontos LIVELO expirando hoje! |
| **Type** | Financial Phishing (Fake bank reward points expiry) |
| **Language** | Portuguese (Brazilian) |
| **Target** | Brazilian bank customers (Bradesco / Livelo loyalty program) |
 
---
 
## 🔍 Phishing Indicators Found
 
### 1. 🚨 Email Authentication Failures (MXToolbox)
 
All major authentication checks **FAILED**:
 
| Check | Result |
|-------|--------|
| DMARC Compliant | ❌ FAILED — No DMARC Record Found |
| SPF Alignment | ❌ FAILED |
| SPF Authenticated | ❌ FAILED |
| DKIM Alignment | ❌ FAILED |
| DKIM Authenticated | ❌ FAILED |
 
> **Conclusion:** The sending domain has no email authentication configured, a strong indicator of spoofing. Legitimate banks always have SPF, DKIM, and DMARC configured.
 
---
 
### 2. 🌐 Malicious Originating IP Address (VirusTotal)
 
| Field | Details |
|-------|---------|
| **IP Address** | `137.184.34.4` |
| **ASN** | AS14061 — DigitalOcean, LLC (US) |
| **Detection** | 1/91 security vendors flagged as **Malicious** |
| **Flagged by** | Criminal IP → Malicious |
| **Suspicious by** | GreyNoise, AlphaSOC |
 
> **Conclusion:** The email originated from a DigitalOcean VPS (cloud server), not from an official Bradesco mail server. Legitimate banks use dedicated corporate mail infrastructure, not shared cloud hosting.
 
---
 
### 3. 📨 Email Relay / Hop Analysis (EML Analyzer)
 
| Hop | From | By | Protocol |
|-----|------|----|----------|
| 1 | — | — | 2023-09-19T18:35:49Z |
| 2 | `137.184.34.4` | bn8nam11ft066.mail.protection.outlook.com | Microsoft SMTP (TLS 1.2) |
| 3 | Microsoft EOP servers | outlook.office365.com | Microsoft SMTP (TLS 1.2) |
 
**Key Observations:**
- Email **originated from IP 137.184.34.4** (DigitalOcean VPS) — not from Bradesco's servers
- Routed through **Microsoft Exchange Online Protection (EOP)** — attacker used a legitimate mail relay to bypass filters
- **Hop 1 is missing** origin data — a common tactic to hide the true source
---
 
### 4. 🧩 OLE Attachment Analysis (EML Analyzer)
 
| Check | Result |
|-------|--------|
| OLE Suspicious Files | ✅ None found (N/A) |
 
> No malicious macro-embedded Office documents were attached. The attack vector was likely a **malicious link** in the email body.
 
---
 
### 5. ⚠️ Social Engineering Tactics
 
| Tactic | Description |
|--------|-------------|
| **Urgency** | "expirando hoje!" (expiring today!) — creates panic to act fast |
| **Authority** | Impersonates **Bradesco** — a major Brazilian bank |
| **Reward Lure** | Claims 92,990 loyalty points are about to expire |
| **Targeted** | Aimed at "CLIENTE PRIME" (premium bank customers) |
 
---
 
## 📊 Summary of Phishing Indicators
 
| # | Indicator | Severity |
|---|-----------|----------|
| 1 | No DMARC record on sending domain | 🔴 High |
| 2 | SPF authentication failed | 🔴 High |
| 3 | DKIM authentication failed | 🔴 High |
| 4 | Originating IP flagged as malicious (DigitalOcean VPS) | 🔴 High |
| 5 | Missing Hop 1 origin — hidden source | 🟠 Medium |
| 6 | Urgent language ("expiring today!") | 🟠 Medium |
| 7 | Impersonation of a major financial institution | 🔴 High |
| 8 | Email relayed through Microsoft EOP to bypass filters | 🟠 Medium |
 
---
 
## 🧠 Key Concepts Learned
 
- **Phishing**: A social engineering attack that tricks users into revealing sensitive information by impersonating a trusted entity.
- **Email Spoofing**: Forging the sender's address to appear as a legitimate source.
- **SPF (Sender Policy Framework)**: A DNS record that specifies which IPs are allowed to send email for a domain.
- **DKIM (DomainKeys Identified Mail)**: A cryptographic signature that verifies email integrity.
- **DMARC (Domain-based Message Authentication, Reporting & Conformance)**: A policy that tells receiving servers what to do when SPF/DKIM fails.
- **Header Analysis**: Examining email metadata to trace origin, relay path, and authentication status.
---
 
## ✅ Conclusion
 
This email is a **confirmed phishing attempt** targeting Brazilian banking customers. It fails all email authentication checks (SPF, DKIM, DMARC), originates from a flagged cloud VPS IP, hides its true origin, and uses urgent financial language to manipulate victims. No legitimate bank email would exhibit these characteristics.
 
---
