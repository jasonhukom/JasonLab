[← Back to Java](../README.md)

# GanjilGenap: Odd / Even

> Type two numbers and see every number in between labelled as **odd (ganjil)** or **even (genap)**, with an attempt to flag **primes (prima)**.

**Status:** 🚧 Odd/even labelling works; the prime check is experimental and also prints a debug line for each number.

## ⚙️ How it works

1. Asks for the first and the last number of a range.
2. Loops through the range and prints `<n>  Bilangan Ganjil` or `<n>  Bilangan Genap`.
3. Uses a square-root based check to add `(Prima)` for primes.
4. Asks `Apakah mau mencoba data yang lain? (Y/n)` to go again.

## ▶️ Run it

```bash
javac GanjilGenap.java
java GanjilGenap
```
