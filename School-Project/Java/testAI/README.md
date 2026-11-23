[← Back to Java](../README.md)

# testAI: Object-oriented exercise

> **Object-oriented programming (PBO)** practice: describe objects found around school as Java classes.

**Status:** ✅ Works

## 🏫 The idea

A parent class `bendaSekolah` ("school object") knows a name and prints a boxed description table. Four child classes extend it and add their own properties and action:

| Class | Extra data | Its action |
| --- | --- | --- |
| `terminalStopKontak` (power strip) | number of holes, colour, cable condition | `salurkanListrik()` |
| `airKolam` (pond water) | colour, condition, type of water | `mengalirkanListrik()` |
| `wastafel` (sink) | colour of the tap | `bukaKeran()` |
| `pohon` (tree) | leaf colour, condition | `fotosintesis()` |

`MainAplikasiPBO` creates one object of each, prints their description tables, runs their actions, and ends with a group-report footer.

## ▶️ Run it

```bash
javac MainAplikasiPBO.java
java MainAplikasiPBO
```
