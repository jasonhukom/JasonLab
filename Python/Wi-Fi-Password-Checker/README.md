[← Back to Python](../README.md)

# Wi-Fi-Password-Checker

Checks your Wi-Fi

---

## 📶 What is this?

A tiny Windows-only script that lists the Wi-Fi networks your PC has connected to before and shows the **saved password** of the one you pick. Handy for finding the password of a network you already joined.

## ⚙️ How it works

1. Runs `netsh wlan show profiles` to list every saved Wi-Fi profile.
2. Prints them as a numbered list.
3. You type a number.
4. Runs `netsh wlan show profile "<name>" key=clear` and prints the details, including the password (under *Key Content*).

## ▶️ Run it

```bash
python wifi-checker.py
```

- Needs **Windows** (it uses the `netsh` command) and Python 3, with no extra packages.
- If the password isn't shown, run the terminal **as Administrator**.

## ⚠️ Use responsibly

Only use it on **your own computer** to recover passwords of networks you're allowed to use.
