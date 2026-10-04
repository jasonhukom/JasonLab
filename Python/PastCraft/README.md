[← Back to Python](../README.md)

# PastCraft

> Story games and a helper tool based on **PastCraft**, a Minecraft survival server and its legends: the Wither War, the Ender Dragon battle, the city of Nipaliterra and more.

| File | What it is | Status |
| --- | --- | --- |
| `pastcraft_game.py` | **Survival PastCraft Server**, a pick-your-adventure game | ✅ |
| `pastcraft_cyoa.py` | **Choose-Your-Ending novel**, a longer interactive story | ❌ syntax error on line 265 |
| `pastcraft_coordinates.py` | Formats Minecraft coordinates as tidy Markdown | ✅ |

The two games were written with help from ChatGPT (credited in the file headers). A copy of both lives in [`../PastCraft_Game`](../PastCraft_Game/README.md).

## 🎮 Survival PastCraft Server

A terminal game where you play a **God** watching over the server. Through five chapters (*Creation of PastCraft*, *Wither War*, *End Battle United*, *Nipaliterra*, *Faxion's Ascent*) you choose which players carry the story forward, and each chapter ends with a small minigame (guess the number, rock-paper-scissors or a quick sum). Your picks and results change the outcome, and a closing screen lists everything that happened. Your choices are typed **hidden** on purpose, so they don't show on screen.

```bash
python3 pastcraft_game.py
```

## 📖 Choose-Your-Ending novel

Pick one of 16 characters (or let the server choose) and read through long story scenes with choices and minigames: a timed quick-time event, number guessing, a quick-typing challenge and a little combat. 

> **To fix:** line 265 has a misplaced bracket in `random.choice([...)]`, so Python refuses to run the file.

## 📍 Coordinates formatter

Asks how many places you want to save, then for each a name and X, Y, Z. It prints a Markdown block per place, ready to paste into notes or Discord:

```bash
python3 pastcraft_coordinates.py
```
