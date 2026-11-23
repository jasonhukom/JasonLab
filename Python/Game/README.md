[← Back to Python](../README.md)

# Space Dodge

> A pygame arcade game: **steer a little red ship and dodge the falling stars** for as long as you can.

**Status:** ✅ Works

## 🎮 How to play

| Key | Action |
| --- | --- |
| ← or **A** | Move left |
| → or **D** | Move right |

- Stars fall from the top, three at a time. They spawn faster and faster as the game goes on.
- Your score is the **time survived**, shown in the top-left corner.
- Touch a star and **You Lost!** appears, then the game closes.

## ▶️ Run it

```bash
pip install pygame
python main.py
```

Run it from this folder: the background picture `bg.jpeg` is loaded relative to the current directory.

## 📁 Files

| File | Purpose |
| --- | --- |
| `main.py` | The whole game |
| `bg.jpeg` | Space background |
| `.vscode/settings.json` | VS Code setting: format Python with Black |
