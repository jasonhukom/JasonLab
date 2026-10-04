[← Back to HTML-CSS-JS](../README.md)

# Bible-Old-Plan

> **A calendar web page for tracking a Bible reading plan.** Upload a plan, tick off each day you read, and mark the days you missed.

## ✝️ What is this?

A single-file web app (`index.html`: HTML + CSS + JavaScript, no libraries). You upload a reading plan as a CSV file and it draws a Sunday–Saturday calendar with one passage per day.

## ✨ Features

- **Upload a CSV plan**, such as the ones in [`CSV/Bible-CSV`](../../../CSV/Bible-CSV/README.md). Short book names like `Gen` or `Mat` are expanded to *Genesis*, *Matthew*, …
- **✔ button**: mark a day's reading as done (the cell turns green).
- **✖ button**: mark a day as missed (the cell turns grey).
- **Drag and drop**: drag a passage onto another day to swap them.
- **Progress is saved** in your browser (`localStorage`), so it's still there when you come back. *Reset Saved Progress* clears it.
- A random Bible verse at the top and a live clock.

## ▶️ How to use

1. Open `index.html` in any modern browser.
2. Click **Upload your bibleplan.csv** and choose a plan (any `.csv` with the date in the first column and the passage in the second).
3. Tick off your readings.

> Your progress lives in that browser only. A different browser or device starts empty.
