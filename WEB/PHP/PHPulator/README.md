[← Back to PHP](../README.md)

# PHPulator · Sonculator

> **Sonculator**: a web calculator in PHP. Enter two numbers, press `+`, `-`, `*` or `/`, and the sum, difference, product or quotient appears on the page.

**Status:** ✅ Works

## ⚙️ How it works

`Sonculator/son.php` holds four small functions (`tambah`, `kurang`, `kali`, `bagi`, which mean add, subtract, multiply and divide) and an HTML form. Each button submits the form with a different operator, and PHP prints a line such as `Hasil: 6 * 7 = 42`. The inputs are escaped with `htmlspecialchars`.

*Angka* = number, *Hasil* = result. The same program is also in the school practicums as `praktikum6/tugas`.

## ▶️ Run it

PHP has to run on a server, so opening the file directly won't work:

```bash
cd Sonculator
php -S localhost:8000
```

Then open <http://localhost:8000/son.php>.
