[← Back to JasonLab](../README.md)

# Python

> Python programs: calculators, text games, pygame games and small tools.

| Project | What it is | Needs | Status |
| --- | --- | --- | --- |
| [`Calculator/`](Calculator/README.md) | Two calculators: a huge formula library and a friendly console one | – | ❌ / ✅ |
| [`Face_Scanner/`](Face_Scanner/README.md) | Face-based attendance system (skeleton) | `opencv-python` | 🚧 |
| [`Game/`](Game/README.md) | **Space Dodge**: dodge falling stars | `pygame` | ✅ |
| [`Hello_World/`](Hello_World/README.md) | Hello world and a date/time test | – | ✅ |
| [`PastCraft/`](PastCraft/README.md) | Story games based on a Minecraft server (plus a coordinate formatter) | – | ✅ / ❌ |
| [`PastCraft_Game/`](PastCraft_Game/README.md) | Copy of the two PastCraft story games | – | ✅ / ❌ |
| [`Pygame/`](Pygame/README.md) | **Mushrams: Power Up!** prototype | `pygame` | 🚧 |
| [`The Seeker/`](The%20Seeker/README.md) | Detective text adventure | Linux/macOS terminal | ❌ |
| [`Wi-Fi-Password-Checker/`](Wi-Fi-Password-Checker/README.md) | Shows saved Wi-Fi passwords on Windows | Windows | ✅ |
| [`Word_Changer/`](Word_Changer/README.md) | Find-and-replace words in a paragraph | – | 🚧 |

## ▶️ Running

```bash
python3 script.py
```

Install the extra packages only when a project needs them:

```bash
pip install pygame          # Game, Pygame
pip install opencv-python   # Face_Scanner
```

Tip: use a virtual environment (`python3 -m venv .venv && source .venv/bin/activate`; on Windows `.venv\Scripts\activate`).
