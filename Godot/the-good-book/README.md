[← Back to Godot](../README.md)

# The Good Book

> **A 2D pixel-art prototype in Godot 4.4**: a spinning pixel earth, a small animated character, and a big *HELLO WORLD!* label in a pixel font.

**Status:** 🚧 Early prototype (no scripts yet, so nothing is interactive)

## 🎮 What's in it?

| Scene | What it contains |
| --- | --- |
| `the_good_book.tscn` | The main scene: puts the character, the earth, a camera and the text together |
| `earth.tscn` | Animated earth sprite (7 frames from a sprite sheet) with a circular collision shape |
| `character_body_2d.tscn` | The animated character (`earthling` animation) with a collision shape |
| `text.tscn` | Label that says *HELLO WORLD!* in the Pixelated Elegance font |

## 📁 Assets

| Folder | Contents |
| --- | --- |
| `assets/Artwork/` | Pixel-art sprite sheet (17×17 px frames) |
| `assets/Pixel Elegant Font/` | *Pixelated Elegance* font (marked public domain in `info.txt`) |
| `assets/Music and Stuff/` | Four tracks: `beginning`, `intro`, `level up 2`, `new world`. They aren't connected to any scene yet |

## ▶️ Run it

1. Open the project in **Godot 4.4** (Import → `project.godot`).
2. Open `the_good_book.tscn` and press **F6** (*Run Current Scene*).

> Pressing **F5** runs the project's *main scene*, which is currently set to `character_body_2d.tscn` (just the character), not `the_good_book.tscn`. Change it in *Project → Project Settings → Application → Run* if you want F5 to start the full scene.
