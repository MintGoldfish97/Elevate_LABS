
# Vulnerability Assessment of Metasploitable 2 Using Tenable Nessus

## Overview

This project demonstrates the process of conducting a vulnerability assessment on a vulnerable Linux virtual machine, Metasploitable 2, using Tenable Nessus Essentials. The objective is to identify security weaknesses, analyze the findings, and understand the potential risks associated with exposed services and outdated software.

## Objectives

* Perform a vulnerability assessment using Nessus Essentials.
* Identify open ports and running services.
* Detect known vulnerabilities and misconfigurations.
* Analyze the severity and impact of discovered vulnerabilities.
* Develop recommendations for remediation and security improvement.

## Lab Environment

### Attacker Machine

* Operating System: Kali Linux
* Tool: Tenable Nessus Essentials

### Target Machine

* Operating System: Metasploitable 2
* Purpose: Intentionally vulnerable machine for security testing

### Network Configuration

* Virtual Environment: VirtualBox
* Network Mode: NAT Network / Host-Only Adapter
* Connectivity verified between Kali Linux and Metasploitable 2.

## Methodology

### 1. Host Discovery

Verified connectivity between the attacker and target systems using network utilities.

### 2. Nessus Configuration

* Installed and activated Nessus Essentials.
* Created a new Basic Network Scan policy.
* Specified the target IP address of the Metasploitable 2 machine.

### 3. Vulnerability Scanning

* Launched the scan.
* Allowed Nessus to perform service detection and vulnerability checks.
* Collected scan results upon completion.

### 4. Analysis

Reviewed findings based on:

* Critical vulnerabilities
* High vulnerabilities
* Medium vulnerabilities
* Low vulnerabilities
* Informational findings

## Key Findings

Common vulnerabilities identified on Metasploitable 2 may include:

* Outdated FTP services
* Vulnerable SSH configurations
* Samba vulnerabilities
* Insecure Telnet service
* Vulnerable web applications
* Weak SSL/TLS configurations
* Outdated software packages
* Remote code execution vulnerabilities

## Risk Assessment

| Severity      | Description                                                   |
| ------------- | ------------------------------------------------------------- |
| Critical      | Vulnerabilities that may allow complete system compromise     |
| High          | Significant security weaknesses requiring immediate attention |
| Medium        | Security issues that could aid an attacker                    |
| Low           | Minor security concerns                                       |
| Informational | General system information and observations                   |

## Recommendations

* Disable unnecessary services.
* Apply security patches and updates.
* Replace insecure protocols such as Telnet with SSH.
* Implement strong authentication mechanisms.
* Restrict network access through firewall rules.
* Regularly perform vulnerability assessments.
* Monitor systems for suspicious activity.

## Tools Used

* Tenable Nessus Essentials
* Kali Linux
* Metasploitable 2
* VirtualBox

## Skills Demonstrated

* Vulnerability Assessment
* Vulnerability Analysis
* Network Security
* Risk Identification
* Security Reporting
* Nessus Administration
* Security Remediation Planning

## Disclaimer

This assessment was performed in a controlled lab environment using Metasploitable 2, an intentionally vulnerable system designed for educational and security training purposes. No unauthorized testing was conducted against production systems.

## Author

Harish S

Cybersecurity Enthusiast | Vulnerability Assessment | Network Security | Threat Hunting
