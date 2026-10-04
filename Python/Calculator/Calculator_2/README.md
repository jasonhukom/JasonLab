[← Back to Calculator](../README.md)

# Calculator 2 · The Ultimate Pyculator

> A **huge library of math formulas** written as Python functions, using nothing but the built-in `math` module. Circle formulas first, then algebra, calculus, trigonometry, geometry, statistics and more.

**Status:** ❌ Can't be imported or run yet: the interactive menu at the bottom of `calculator_2.py` is unfinished and causes a `SyntaxError` (around line 2462). Remove or finish that unfinished `main()` and the formula library works on its own (checked: it loads and the formulas return correct results).

## 🧮 What's inside

`calculator_2.py` has over **700 one-line formulas** (lambdas) and **150+ helper functions**, grouped into sections:

| Area | Examples |
| --- | --- |
| **Basics & constants** | add, subtract, multiply, divide, `PI`, `E`, `TAU`, rounding helpers |
| **Algebra** | fractions, powers/roots/percentages, logarithms, quadratic roots, polynomials, interpolation |
| **Number theory & combinatorics** | primes, LCM/GCD, Möbius, factorials, sequences & series, permutations/combinations |
| **Calculus & numerics** | numerical derivatives and integrals, root finding, optimisation, differential equations, Taylor series |
| **Trigonometry** | degrees and radians, identities, right triangles, hyperbolic functions, waves |
| **Geometry** | circle, ellipse, triangles, quadrilaterals, regular polygons, cube, sphere, cylinder, cone, pyramids, prisms, Platonic solids, centroids, conic sections |
| **Coordinate geometry & vectors** | 2D/3D coordinates, vectors, planes and lines |
| **Linear algebra** | matrices (determinant, power, …) and complex numbers |
| **Statistics & probability** | descriptive stats, distributions, inference, regression/fitting |
| **Finance** | interest and related formulas |

## 🏷️ Naming rules

Functions are named `<topic>_<what>_<given>`, for example `circle_area_r_pi` = "area of a circle, given the radius".

- A name ending in **`_pi`** returns a plain number with π already worked out.
- A name **without `_pi`** returns the answer as text, such as `"25π"`.
- Angles are in **degrees** unless the name says `_rad`.
- `list_formulas("circle_")` lists every function that starts with that prefix.

```python
import calculator_2 as pyc

pyc.circle_area_r_pi(5)      # 78.53981633974483
pyc.circle_area_r(5)         # "25π"
pyc.list_formulas("circle_") # returns the list of circle formulas
```

## 🚧 To finish

- The `main()` menu (*THE ULTIMATE PYCULATOR*: *1) Get Started*, *2) Start Calculating*) is a sketch and needs completing.
