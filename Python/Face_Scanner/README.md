[← Back to Python](../README.md)

# Face_Scanner

> A **face-based attendance system for a school**: a webcam spots a student's face, and the program records when they arrive and leave, marking them on time or late.

**Status:** 🚧 Early skeleton. The attendance rules and webcam preview exist; face recognition and the database are still to be written.

## 🧩 What's here

| File | What it does today |
| --- | --- |
| `src/camera.py` | Opens the webcam in an OpenCV window. Press **`q`** to quit. Run it with `python -m src.camera` |
| `src/attendance_logic.py` | The IN/OUT logic (below) |
| `src/database.py` | Only `import sqlite3` so far. The save/load functions are still to be written |
| `main.py`, `requirements.txt` | Empty placeholders |

## 📋 Attendance rules (`attendance_logic.py`)

- **First scan of the day** → status `IN`, noted as `ON_TIME` or `LATE` (the school start time is set to `07:30`).
- **Later scans** → flip between `IN` and `OUT` (for example when leaving after school).
- **Scans less than 5 minutes apart** are blocked as duplicates (`BLOCKED`, "Too fast").
- It expects two functions from `database.py`, `get_last_attendance` and `save_attendance`, which don't exist yet.

## 🗺️ Next steps

1. Write the `database.py` functions with SQLite.
2. Add face detection and recognition, then call `process_attendance(user_id)` for each recognised face.
3. Fill in `main.py` and `requirements.txt`.

## ▶️ Try the camera

```bash
pip install opencv-python
python -m src.camera
```
