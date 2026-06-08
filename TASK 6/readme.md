# 🔐 Task 6: Create a Strong Password and Evaluate Its Strength

**Cybersecurity Internship | ElevateLabs**

---

## 📌 Objective

Understand what makes a password strong, test passwords with varying complexity against online strength checkers, and document findings on password security best practices.

---

## 🛠️ Tools Used

- [passwordmeter.com](https://passwordmeter.com) — Detailed scoring with character analysis
-

---

## 🔑 Passwords Tested

| # | Password | Length | Complexity Level |
|---|----------|--------|-----------------|
| 1 | `password123` | 11 | Weak |
| 2 | `Password@123` | 10 | Fair |
| 3 | `MyD0g$Name!sMax` | 16 | Strong |
| 4 | `T#9mK!vQ2@nXpL5z` | 17 | Very Strong |
| 5 | `Purple!Monkey$Jumps#Over7Clouds` | 31 | Very Strong (Passphrase) |

> ⚠️ **Note:** These passwords were created only for educational testing. Never use sample passwords from tutorials for real accounts.

---

## 📊 Strength Evaluation Results

### Password 1 — `password123`
- **Score:** ~10% (Very Weak)
- **Issues:** Common dictionary word, no symbols, predictable number suffix
- **Crack Time:** Instantly cracked by dictionary attack

### Password 2 — `Pass@1234`
- **Score:** ~45% (Medium)
- **Issues:** Short, common pattern (`@` substitution is well-known), sequential numbers
- **Crack Time:** Minutes to hours via hybrid attack

### Password 3 — `MyD0g$Name!sMax`
- **Score:** ~78% (Strong)
- **Strengths:** Mixed case, symbols, numbers, no dictionary word
- **Crack Time:** Several years via brute force

### Password 4 — `T#9mK!vQ2@nXpL5z`
- **Score:** ~95% (Very Strong)
- **Strengths:** Fully random, high entropy, all character types
- **Crack Time:** Centuries via brute force

### Password 5 — `Purple!Monkey$Jumps#Over7Clouds`
- **Score:** ~98% (Very Strong)
- **Strengths:** Long passphrase with symbols and numbers, easy to memorize, very high entropy
- **Crack Time:** Practically uncrackable

---

## 🧠 Key Concepts

### What Makes a Password Strong?
A strong password has:
- **Length** — Minimum 12–16 characters; longer is always better
- **Uppercase letters** — A–Z
- **Lowercase letters** — a–z
- **Numbers** — 0–9
- **Special symbols** — `!@#$%^&*()_+-=`
- **No dictionary words** or personal information
- **No predictable patterns** (e.g., `abc`, `123`, `qwerty`)

---

## ⚔️ Common Password Attacks

### 1. Brute Force Attack
The attacker tries **every possible combination** of characters until the correct password is found.
- **Defense:** Use long passwords (16+ chars). A 16-char random password takes centuries to brute force.

### 2. Dictionary Attack
Uses a pre-built list of **common words, phrases, and leaked passwords** to guess credentials.
- **Defense:** Avoid real words. `password`, `sunshine`, `iloveyou` are in every dictionary list.

### 3. Credential Stuffing
Attackers use **username/password pairs leaked from data breaches** on other sites.
- **Defense:** Use a unique password for every account.

### 4. Phishing
Tricks users into **voluntarily entering their password** on a fake site.
- **Defense:** Enable MFA; verify URLs before logging in.

---

## ✅ Best Practices for Password Security

1. **Use 16+ characters** — Length is the single biggest factor in strength
2. **Mix all character types** — Uppercase, lowercase, numbers, symbols
3. **Avoid personal info** — No birthdays, names, or pet names
4. **Never reuse passwords** — Each account needs its own unique password
5. **Use a password manager** — Tools like Bitwarden or KeePass generate and store strong passwords
6. **Enable Multi-Factor Authentication (MFA)** — Even if a password leaks, MFA blocks attackers
7. **Consider passphrases** — `Correct$Horse!Battery9Staple` is both strong and memorable
8. **Check for breaches** — Use [haveibeenpwned.com](https://haveibeenpwned.com) to see if your email was compromised

---

## 📈 Conclusion

Password complexity directly impacts security. Even going from 8 to 16 characters can change crack time from **hours to centuries**. The most effective strategy combines a long, random password with a password manager and MFA — making accounts practically uncrackable even if one factor is compromised.

---