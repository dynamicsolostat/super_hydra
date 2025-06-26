# 🔐 Smart Brute-Force Login Tool with CAPTCHA Solver

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Platform](https://img.shields.io/badge/Tested%20on-Kali%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

A Python-based brute-force tool that simulates Hydra functionality, with added support for solving basic math CAPTCHAs (e.g., `5 + 3`). Designed for **educational use** in environments like **TryHackMe**, **HackTheBox**, or your own local test servers.

---

## 📦 Features

- ✅ Brute-forces login using username & password lists
- 🧠 Solves simple mathematical CAPTCHAs automatically
- 🚫 Skips invalid usernames to save time
- 📂 Saves results in timestamped log files
- 🧪 Tested on Kali Linux and Flask login apps

---

## 🐧 Kali Linux Installation Guide

### 1. 🔧 System Requirements

- Kali Linux (2022.1 or newer)
- Python 3.10+
- Git
- Internet access (for installing dependencies)

---

### 2. 📁 Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/smart-brute-captcha.git
cd smart-brute-captcha

3. 🐍 Set Up Python Environment (Recommended)

    ### Run these
    sudo apt update
    sudo apt install python3-venv -y
    python3 -m venv venv
    source venv/bin/activate

4. 📦 Install Dependencies
    pip install requests beautifulsoup4


5. 📝 Prepare Input Files

    Create two files in the same folder as smart_brute.py:

        Name the first file "users.txt"
### Some usernames to try
  --> admin
  --> rodney
  --> guest

        Name the second file "passwords.txt"

### Some passwords to try 
    -->admin123
    -->hunter2
    -->guestpass


  ### Here is the ▶️ Usage

        Run the tool with:

            "python3 smart_brute.py"

### It will:

    Check if users exist (based on error messages)

    Attempt all password combinations

    Automatically solve math CAPTCHAs when required

    Stop on the first successful login and save results either to your log file or whatever.