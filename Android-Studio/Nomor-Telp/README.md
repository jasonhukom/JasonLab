[← Back to Android-Studio](../README.md)

# Nomor-Telp

> **A phone-number form app.** Type a number, choose whether it's a home, mobile or office number, tap the button and a pop-up shows the result.

**Status:** ✅ Works

*Nomor Telp* is Indonesian for "phone number".

## 📱 What does it do?

1. A text box takes a phone number (hint: *"Silahkan masukan nomor Anda"*, "Please enter your number").
2. Three radio buttons choose the type: **Telp Rumah** (home), **Mobile**, **Telp Kantor** (office).
3. Tapping the button shows a toast message such as `Mobile:08123456789`.

## 🧰 Tech

| | |
| --- | --- |
| Language | Java |
| UI | XML layout (`ConstraintLayout`, `EditText`, `RadioGroup`, `Button`) |
| Package | `com.example.jasonproject2` |
| Min / target SDK | 29 / 36 |
| Build | Gradle (Kotlin DSL) |

## 📁 Where things are

| Path | Purpose |
| --- | --- |
| `app/src/main/java/com/example/jasonproject2/MainActivity.java` | Reads the text box and radio buttons, shows the toast (`showText`) |
| `app/src/main/res/layout/activity_main.xml` | The screen layout |
| `app/src/main/res/values/strings.xml` | Texts (in Indonesian) |
| `editTextPhone.java`, `radioGroup.java` | Empty placeholder classes |

## ▶️ Run it

Open this folder in Android Studio, let Gradle sync, and press **Run ▶**.
