[← Back to Java](../README.md)

# CV.RPL: Employee salary table

> Enter some employees and get a neat **salary table** that includes their family allowances.

**Status:** ✅ Works

## ⚙️ How it works

For each employee the program asks for:

| Question | Used for |
| --- | --- |
| Name | Shown in the table |
| **Golongan** (grade) `A`, `B` or `C` | Base salary: A = Rp 1,000,000 · B = Rp 750,000 · C = Rp 500,000 |
| Married? (`Y`/`n`) | Spouse allowance = 10 % of base salary |
| Number of children (only if married) | Child allowance = 5 % of base salary per child, counted for up to 4 children |

Gross total (*Gaber*) = base salary + spouse allowance + child allowance. At the end it prints everything in a box-drawn table with amounts formatted as Indonesian Rupiah, and asks whether to enter more data.

Wrong input just asks again ("Input anda salah!").

## ▶️ Run it

```bash
javac cv_rpl.java
java cv_rpl
```
