[← Back to Calculator](../README.md)

# Codedex Calculator

> A friendly **console calculator**: pick two numbers and one of `+ - * /`, confirm, watch a short loading animation, and see the answer.

**Status:** ✅ Works

## ⚙️ How it works

1. Prints a *The Calculator* banner.
2. Asks for the first number, the operator and the second number.
3. Shows the question back and asks to confirm: `(Y/n)`.
4. Plays "Loading…" and "calculating…" countdowns, clears the screen and prints, e.g. `6.0 * 7.0 = 42.0`.
5. Asks whether you want to continue. Choosing no plays an *Exiting…* animation and quits.

It also handles dividing by zero and typing letters instead of numbers.

## ▶️ Run it

```bash
python3 script.py
```

> Answer the yes/no questions with a **capital** `Y` or `N`.
