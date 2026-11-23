[← Back to Android-Studio](../README.md)

# My-App

> **A Jetpack Compose starter app** with three navigation destinations: Home, Favorites and Profile.

**Status:** 🚧 Starter template (the screens only say *Hello Android!*)

## 📱 What is this?

An Android app created from Android Studio's Compose template with the adaptive *Navigation Suite*: a bottom bar on phones that becomes a side rail on larger screens. The three destinations (Home, Favorites, Profile) all show the same greeting for now, so it works as a base to build real screens on.

## 🧰 Tech

| | |
| --- | --- |
| Language | Kotlin |
| UI | Jetpack Compose, Material 3 (`NavigationSuiteScaffold`) |
| Package | `com.doesntexist.myapplication` |
| Min / target SDK | 24 / 36 |
| Build | Gradle (Kotlin DSL) |

## 📁 Where things are

| Path | Purpose |
| --- | --- |
| `app/src/main/java/com/doesntexist/myapplication/MainActivity.kt` | App entry point, navigation and the greeting |
| `app/src/main/java/.../ui/theme/` | Colours, typography and theme |
| `app/src/main/java/.../jasonPresent.java` | Empty interface (placeholder) |
| `CMakeLists.txt` | Placeholder text file, not used by the build |

## ▶️ Run it

Open this folder in Android Studio, let Gradle sync, and press **Run ▶**.
