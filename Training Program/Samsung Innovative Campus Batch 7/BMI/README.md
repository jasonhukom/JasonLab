[← Back to Samsung Innovative Campus Batch 7](../README.md)

# BMI: Health Checker

> Enter your height and weight and find out whether your weight is **healthy, overweight, obese or extremely obese** for your height.

**Status:** ✅ Standard mode works · 🚧 Metric mode is not finished

*The script's first comment, "mengetahui tingkat kesehatan kalian", means "find out your health level".* It's a programming exercise, **not medical advice**.

## ⚙️ How it works

1. Type `standard` or `metric`.
   - **standard**: height in feet and inches, weight in pounds.
   - **metric**: height in cm, weight in kg (converted to feet, inches and pounds).
2. The program looks up your height in a table of weight ranges and prints one of:
   - *Congratulations, your weight is healthy!*
   - *You're overweight!*
   - *You are obese, please eat more healthy food!*
   - *You have extreme obesity, please go to the doctor!*
3. It runs once and exits.

The table covers heights from **4 ft 10 in to 6 ft 4 in**. Heights or weights outside it print *Wrong Input. Please try again.*

## 🚧 Known issue

In metric mode the inches value is stored under a misspelled variable name (`height_std_inch`), so the lookup treats every height as having 0 inches. Use standard mode, or fix that name.

## ▶️ Run it

```bash
python3 BMI.py
```

The file was converted from a notebook (`.ipynb`) to a `.py` script.
