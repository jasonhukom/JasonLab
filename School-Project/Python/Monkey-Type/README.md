[← Back to Python](../README.md)

# Monkey-Type · Typing Speed Test

> A **typing speed test for the terminal**, in the style of Monkeytype. Type the shown text, then see your **accuracy** and **words per minute (WPM)**.

**Status:** ✅ Works on **Linux and macOS** (it uses the `termios` module). On Windows it warns that it might not work.

## 🎮 How it works

1. A random paragraph is picked from five built-in texts. They're in **Indonesian** and about school subjects: programming, maths, language, science and English.
2. Type it. Each character you type turns **green** if it's right and **red** if it's wrong, and the untyped part stays white.
3. The test ends when you finish the text or press **Enter** or **Ctrl+C**.
4. It prints your accuracy and speed.

```text
Accuracy: 96.4%
Speed: 52.3 WPM
```

## ▶️ Run it

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install rich
python3 speed-test.py
```
