[← Back to Java](../../README.md)

# Geometry · Prisculator

> **Prisculator** ("counts your prisms"): enter the corner points of a prism's base and its height, and get the base area, perimeter and volume.

**Status:** ✅ Works (the class is named `Fasculator`)

## ⚙️ How it works

1. Enter the **number of base vertices** (3 for a triangle, 4 for a quadrilateral, …).
2. Enter the `x` and `y` coordinates of each vertex, **in order around the shape**.
3. Enter the **height** of the prism.

It then prints:

| Result | How it's computed |
| --- | --- |
| Base area | Shoelace formula over the coordinates |
| Perimeter | Sum of the distances between neighbouring vertices |
| Volume | Base area × height |

Area and volume are shown both as a `double` and as an `int` (cut off at the decimal point).

## ▶️ Run it

```bash
cd src
javac Fasculator.java
java Fasculator
```
