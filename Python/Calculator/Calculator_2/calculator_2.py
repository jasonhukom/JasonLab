import math

PI = math.pi
E = math.e
TAU = math.tau

# --- Simple Calculator ---
add = lambda x, y: x + y
subtract = lambda x, y: x - y
divide = lambda x, y: x / y
multiply = lambda x, y: x * y

ratio = lambda theta: theta / 360

# --- Circle ---
circle_radius_d = lambda d: d / 2
circle_radius_a_pi = lambda a: math.sqrt(a / PI)
circle_radius_c_pi = lambda c: c / (2 * PI)
circle_diameter_r = lambda r: 2 * r
circle_diameter_a_pi = lambda a: 2 * math.sqrt(a / PI)
circle_diameter_c_pi = lambda c: c / PI
circle_circumference_r_pi = lambda r: 2 * PI * r
circle_circumference_r = lambda r: f"{2 * r}π"
circle_circumference_d_pi = lambda d: PI * d
circle_circumference_d = lambda d: f"{d}π"
circle_circumference_a_pi = lambda a: 2 * PI * circle_radius_a_pi(a)
circle_circumference_a = lambda a: f"{2 * circle_radius_a_pi(a)}π"
circle_area_r_pi = lambda r: PI * (r ** 2)
circle_area_r = lambda r: f"{r ** 2}π"
circle_area_d_pi = lambda d: PI * (circle_radius_d(d) ** 2)
circle_area_d = lambda d: f"{circle_radius_d(d) ** 2}π"
circle_area_c_pi = lambda c: PI * (circle_radius_c_pi(c) ** 2)
circle_area_c = lambda c: f"{circle_radius_c_pi(c) ** 2}π"
circle_arc_length_r_pi = lambda r, theta: circle_circumference_r_pi(r) * (ratio(theta))
circle_arc_length_r = lambda r, theta: f"{(2 * r * (ratio(theta)))}π"
circle_arc_length_d_pi = lambda d, theta: circle_circumference_r_pi(circle_radius_d(d)) * (ratio(theta))
circle_arc_length_d = lambda d, theta: f"{2 * r * (ratio(theta))}π"
circle_arc_length_a_pi = lambda a, theta: circle_circumference_r_pi(circle_radius_a_pi(a)) * (ratio(theta))
circle_arc_length_a = lambda a, theta: f"{2 * (a / PI) * (ratio(theta))}π"
circle_arc_length_c = lambda c, theta: c * (ratio(theta))
circle_sector_area_r_pi = lambda r, theta: circle_area_r_pi(r) * (ratio(theta))
circle_sector_area_r = lambda r, theta: f"{circle_area_r(r) * (ratio(theta))}π"
circle_sector_area_d_pi = lambda d, theta: circle_area_d_pi(d) * (ratio(theta))
circle_sector_area_d = lambda d, theta: f"{(circle_diameter_r(d) ** 2) * (ratio(theta))}π"
circle_sector_area_c_pi = lambda c, theta: circle_area_r_pi(circle_radius_c_pi(c)) * (ratio(theta))
circle_sector_area_c = lambda c, theta: f"{(circle_radius_c_pi(c) ** 2) * (ratio(theta))}π"
circle_sector_area_a_pi = lambda a, theta: circle_area_r_pi(circle_radius_a_pi(a)) * (ratio(theta))
circle_arc_chord_r = lambda r, theta: circle_diameter_r(r) * math.sin(math.radians(theta) / 2)
circle_arc_chord_d = lambda d, theta: d * math.sin(math.radians(theta) / 2)



# ======================================================================
#  MATH FORMULA LIBRARY  (added below -- pure Python, `math` module only)
#
#  Naming follows the circle section above:
#      <topic>_<what>_<given>            e.g.  sphere_volume_r_pi
#      *_pi    -> numeric answer, with π already worked out
#      no _pi  -> symbolic answer as a string such as "12.5π"
#                 (only used where the formula really contains π)
#  Angles are in DEGREES unless the name says _rad.
#  Call list_formulas("prefix") to see every function and its arguments.
# ======================================================================

# --- Extra Constants ---
PHI = (1 + math.sqrt(5)) / 2
SQRT2 = math.sqrt(2)
SQRT3 = math.sqrt(3)
SQRT5 = math.sqrt(5)
LN2 = math.log(2)
LN10 = math.log(10)
EULER_GAMMA = 0.5772156649015329


def _with_pi(coefficient):
    """Formats a symbolic answer such as 12π (whole-number floats lose the .0)."""
    if isinstance(coefficient, float) and coefficient.is_integer():
        coefficient = int(coefficient)
    return f"{coefficient}π"


# --- Utilities & Rounding ---
sign = lambda x: (x > 0) - (x < 0)
absolute = lambda x: abs(x)
clamp = lambda x, low, high: max(low, min(x, high))
lerp = lambda a, b, t: a + (b - a) * t
inverse_lerp = lambda a, b, value: (value - a) / (b - a)
map_range = lambda x, in_min, in_max, out_min, out_max: out_min + (x - in_min) * (out_max - out_min) / (in_max - in_min)
is_close = lambda a, b, rel_tol=1e-9, abs_tol=1e-12: math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)
fractional_part = lambda x: x - math.trunc(x)
round_to = lambda x, digits=0: round(x, digits)
round_up = lambda x, digits=0: math.ceil(x * 10 ** digits) / 10 ** digits
round_down = lambda x, digits=0: math.floor(x * 10 ** digits) / 10 ** digits
truncate = lambda x, digits=0: math.trunc(x * 10 ** digits) / 10 ** digits
ceiling = lambda x: math.ceil(x)
floor = lambda x: math.floor(x)


def significant_figures(x, n):
    """Rounds x to n significant figures."""
    if x == 0:
        return 0.0
    return round(x, n - int(math.floor(math.log10(abs(x)))) - 1)


def scientific_notation(x):
    """Returns (mantissa, exponent) so that x = mantissa * 10**exponent."""
    if x == 0:
        return 0.0, 0
    exponent = int(math.floor(math.log10(abs(x))))
    return x / 10 ** exponent, exponent


# --- Fractions ---
def simplify_fraction(numerator, denominator):
    """Reduces a fraction of integers to lowest terms, e.g. (6, -8) -> (-3, 4)."""
    if denominator == 0:
        raise ZeroDivisionError("denominator cannot be 0")
    g = math.gcd(numerator, denominator)
    if denominator < 0:
        g = -g
    return numerator // g, denominator // g


fraction_add = lambda n1, d1, n2, d2: simplify_fraction(n1 * d2 + n2 * d1, d1 * d2)
fraction_subtract = lambda n1, d1, n2, d2: simplify_fraction(n1 * d2 - n2 * d1, d1 * d2)
fraction_multiply = lambda n1, d1, n2, d2: simplify_fraction(n1 * n2, d1 * d2)
fraction_divide = lambda n1, d1, n2, d2: simplify_fraction(n1 * d2, d1 * n2)


def mixed_number(numerator, denominator):
    """Improper fraction -> (whole, numerator, denominator), e.g. (7, 3) -> (2, 1, 3)."""
    negative = (numerator < 0) != (denominator < 0)
    whole, remainder = divmod(abs(numerator), abs(denominator))
    n, d = simplify_fraction(remainder, abs(denominator))
    if whole == 0:
        return 0, (-n if negative else n), d
    return (-whole if negative else whole), n, d


def decimal_to_fraction(x, max_denominator=1000000):
    """Best fraction for a decimal using continued fractions, e.g. 0.75 -> (3, 4)."""
    negative = x < 0
    x = abs(x)
    h2, h1, k2, k1 = 0, 1, 1, 0
    y = x
    while True:
        a = math.floor(y)
        h = a * h1 + h2
        k = a * k1 + k2
        if k > max_denominator:
            break
        h2, h1, k2, k1 = h1, h, k1, k
        if abs(x - h1 / k1) < 1e-12 or y == a:
            break
        y = 1 / (y - a)
    return (-h1 if negative else h1), k1


def continued_fraction(x, terms=10):
    """First `terms` coefficients of the continued fraction of x."""
    result = []
    for _ in range(terms):
        a = math.floor(x)
        result.append(a)
        if x == a:
            break
        x = 1 / (x - a)
    return result


# --- Powers, Roots & Percentages ---
power = lambda base, exponent: base ** exponent
square = lambda x: x ** 2
cube = lambda x: x ** 3
square_root = lambda x: math.sqrt(x)
reciprocal = lambda x: 1 / x
modulo = lambda x, y: x % y
floor_divide = lambda x, y: x // y
hypotenuse_nd = lambda *values: math.hypot(*values)
isqrt = lambda n: math.isqrt(n)


def nth_root(x, n):
    """Real n-th root of x (odd roots of negative numbers are allowed)."""
    if x < 0:
        if n != int(n) or int(n) % 2 == 0:
            raise ValueError("only odd integer roots of negative numbers are real")
        return -((-x) ** (1 / n))
    return x ** (1 / n)


cube_root = lambda x: nth_root(x, 3)


def sqrt_babylonian(x, iterations=100):
    """Square root by the Babylonian (Heron) method: guess = (guess + x / guess) / 2."""
    if x < 0:
        raise ValueError("x must be >= 0")
    if x == 0:
        return 0.0
    guess = math.ldexp(1.0, math.frexp(x)[1] // 2)
    for _ in range(iterations):
        better = (guess + x / guess) / 2
        if better == guess:
            break
        guess = better
    return guess


percent_of = lambda percent, x: x * percent / 100
what_percent = lambda part, whole: part / whole * 100
percent_change = lambda old, new: (new - old) / old * 100
percent_increase = lambda x, percent: x * (1 + percent / 100)
percent_decrease = lambda x, percent: x * (1 - percent / 100)
percent_difference = lambda a, b: abs(a - b) / ((a + b) / 2) * 100
proportion_fourth = lambda a, b, c: b * c / a          # a : b = c : x  ->  x
scale_factor = lambda new_length, old_length: new_length / old_length

# --- Logarithms & Exponentials ---
ln = lambda x: math.log(x)
log10 = lambda x: math.log10(x)
log2 = lambda x: math.log2(x)
exp = lambda x: math.exp(x)
log_base = lambda x, base: math.log(x) / math.log(base)
antilog10 = lambda x: 10 ** x
exponential_growth = lambda start, rate, t: start * math.exp(rate * t)
exponential_decay = lambda start, rate, t: start * math.exp(-rate * t)
half_life_remaining = lambda start, t, half_life: start * 0.5 ** (t / half_life)
half_life_from_rate = lambda rate: math.log(2) / rate
doubling_time_continuous = lambda rate: math.log(2) / rate
doubling_time_compound = lambda rate: math.log(2) / math.log(1 + rate)
logistic_growth = lambda capacity, start, rate, t: capacity / (1 + ((capacity - start) / start) * math.exp(-rate * t))
sigmoid = lambda x: 1 / (1 + math.exp(-x)) if x >= 0 else math.exp(x) / (1 + math.exp(x))
logit = lambda p: math.log(p / (1 - p))
softplus = lambda x: math.log1p(math.exp(-abs(x))) + max(x, 0)


def softmax(values):
    """Turns a list of scores into probabilities that add up to 1."""
    top = max(values)
    exps = [math.exp(v - top) for v in values]
    total = sum(exps)
    return [v / total for v in exps]


# --- Special Functions ---
gamma = lambda x: math.gamma(x)
log_gamma = lambda x: math.lgamma(x)
beta_function = lambda a, b: math.exp(math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b))
erf = lambda x: math.erf(x)
erfc = lambda x: math.erfc(x)
stirling_approximation = lambda n: math.sqrt(2 * PI * n) * (n / E) ** n
sinc = lambda x: 1.0 if x == 0 else math.sin(x) / x
sinc_normalized = lambda x: 1.0 if x == 0 else math.sin(PI * x) / (PI * x)


def riemann_zeta(s, terms=1000):
    """Riemann zeta function for s > 1 (partial sum + Euler-Maclaurin tail)."""
    if s <= 1:
        raise ValueError("this formula needs s > 1")
    n = terms
    total = sum(k ** -s for k in range(1, n))
    return total + n ** (1 - s) / (s - 1) + n ** -s / 2 + s * n ** (-s - 1) / 12


def lambert_w(x, tolerance=1e-14):
    """Principal branch of the Lambert W function: solves w * e^w = x (x >= -1/e)."""
    if x < -1 / E - 1e-15:
        raise ValueError("x must be >= -1/e")
    if x == 0:
        return 0.0
    if abs(x + 1 / E) < 1e-15:
        return -1.0
    if x < -0.25:
        w = -1 + math.sqrt(max(0.0, 2 * (E * x + 1)))
    elif x < 3:
        w = math.log1p(x)
    else:
        w = math.log(x) - math.log(math.log(x))
    for _ in range(100):
        ew = math.exp(w)
        f = w * ew - x
        step = f / (ew * (w + 1) - (w + 2) * f / (2 * w + 2))
        w -= step
        if abs(step) < tolerance * (1 + abs(w)):
            break
    return w


def agm(a, b, max_iterations=100):
    """Arithmetic-geometric mean of a and b."""
    for _ in range(max_iterations):
        if abs(a - b) <= 1e-15 * max(abs(a), abs(b)):
            break
        a, b = (a + b) / 2, math.sqrt(a * b)
    return a


elliptic_k_complete = lambda m: PI / (2 * agm(1, math.sqrt(1 - m)))     # K(m), parameter m = k^2, m < 1

# --- Ways to Approximate π and e ---
pi_leibniz = lambda terms: 4 * sum((-1) ** k / (2 * k + 1) for k in range(terms))
pi_wallis = lambda terms: 2 * math.prod((4 * k * k) / (4 * k * k - 1) for k in range(1, terms + 1))
pi_nilakantha = lambda terms: 3 + sum((-1) ** (k + 1) * 4 / ((2 * k) * (2 * k + 1) * (2 * k + 2)) for k in range(1, terms + 1))
pi_machin = lambda: 4 * (4 * math.atan(1 / 5) - math.atan(1 / 239))
pi_basel = lambda terms: math.sqrt(6 * sum(1 / k ** 2 for k in range(1, terms + 1)))
e_series = lambda terms: sum(1 / math.factorial(k) for k in range(terms))
e_limit = lambda n: (1 + 1 / n) ** n
golden_ratio_continued_fraction = lambda depth: (lambda f: f(f, depth))(lambda self, d: 1.0 if d == 0 else 1 + 1 / self(self, d - 1))


def pi_ramanujan(terms=3):
    """Ramanujan's 1914 series for 1/π (about 8 digits per term)."""
    total = sum(math.factorial(4 * k) * (1103 + 26390 * k) / (math.factorial(k) ** 4 * 396 ** (4 * k)) for k in range(terms))
    return 1 / (2 * SQRT2 / 9801 * total)


def pi_chudnovsky(terms=3):
    """Chudnovsky series (about 14 digits per term)."""
    total = sum((-1) ** k * math.factorial(6 * k) * (13591409 + 545140134 * k) / (math.factorial(3 * k) * math.factorial(k) ** 3 * 640320 ** (3 * k)) for k in range(terms))
    return 426880 * math.sqrt(10005) / total

# --- Number Theory ---
def gcd(*numbers):
    """Greatest common divisor of any amount of integers."""
    return math.gcd(*numbers)


def lcm(*numbers):
    """Least common multiple of any amount of integers."""
    return math.lcm(*numbers)


def extended_gcd(a, b):
    """Returns (g, x, y) such that a*x + b*y = g = gcd(a, b)."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t


def mod_inverse(a, m):
    """The x with (a * x) % m == 1."""
    g, x, _ = extended_gcd(a % m, m)
    if g != 1:
        raise ValueError("no modular inverse: a and m are not coprime")
    return x % m


mod_pow = lambda base, exponent, modulus: pow(base, exponent, modulus)
is_coprime = lambda a, b: math.gcd(a, b) == 1


def chinese_remainder(remainders, moduli):
    """Smallest x >= 0 with x % moduli[i] == remainders[i] (moduli must be pairwise coprime)."""
    total = 1
    for m in moduli:
        total *= m
    result = 0
    for r, m in zip(remainders, moduli):
        partial = total // m
        result += r * partial * mod_inverse(partial, m)
    return result % total


def is_prime(n):
    """True if n is prime (Miller-Rabin, deterministic for n < 3.3e24)."""
    if n < 2:
        return False
    bases = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in bases:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in bases:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def prime_factors(n):
    """Prime factors with repeats, smallest first, e.g. 360 -> [2, 2, 2, 3, 3, 5]."""
    factors = []
    if n < 2:
        return factors
    for p in (2, 3):
        while n % p == 0:
            factors.append(p)
            n //= p
    i = 5
    while i * i <= n:
        for p in (i, i + 2):
            while n % p == 0:
                factors.append(p)
                n //= p
        i += 6
    if n > 1:
        factors.append(n)
    return factors


def prime_factorization(n):
    """Prime factorisation as {prime: exponent}, e.g. 360 -> {2: 3, 3: 2, 5: 1}."""
    result = {}
    for p in prime_factors(n):
        result[p] = result.get(p, 0) + 1
    return result


def primes_up_to(n):
    """All primes <= n (sieve of Eratosthenes)."""
    if n < 2:
        return []
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, math.isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
    return [i for i, flag in enumerate(sieve) if flag]


def nth_prime(n):
    """The n-th prime (1 -> 2, 2 -> 3, 3 -> 5 ...)."""
    if n < 1:
        raise ValueError("n must be >= 1")
    if n < 6:
        return (2, 3, 5, 7, 11)[n - 1]
    limit = int(n * (math.log(n) + math.log(math.log(n)))) + 10
    return primes_up_to(limit)[n - 1]


def next_prime(n):
    """Smallest prime greater than n."""
    n += 1
    while not is_prime(n):
        n += 1
    return n


def previous_prime(n):
    """Largest prime smaller than n."""
    n -= 1
    while n >= 2 and not is_prime(n):
        n -= 1
    if n < 2:
        raise ValueError("there is no smaller prime")
    return n


prime_count = lambda x: len(primes_up_to(x))
prime_count_approx = lambda x: x / math.log(x)


def goldbach_pair(n):
    """Two primes that add up to the even number n (n > 2)."""
    for p in range(2, n // 2 + 1):
        if is_prime(p) and is_prime(n - p):
            return p, n - p
    raise ValueError("n must be an even number greater than 2")


def divisors(n):
    """All positive divisors of n, in order."""
    small, large = [], []
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            small.append(i)
            if i != n // i:
                large.append(n // i)
    return small + large[::-1]


def divisor_count(n):
    """How many positive divisors n has."""
    result = 1
    for exponent in prime_factorization(n).values():
        result *= exponent + 1
    return result


def divisor_sum(n):
    """Sum of all positive divisors of n (sigma function)."""
    result = 1
    for p, e in prime_factorization(n).items():
        result *= (p ** (e + 1) - 1) // (p - 1)
    return result


def euler_totient(n):
    """How many numbers from 1..n are coprime to n."""
    result = n
    for p in prime_factorization(n):
        result -= result // p
    return result


def mobius(n):
    """Möbius function: 0 if n has a squared factor, else (-1)^(number of prime factors)."""
    factors = prime_factorization(n)
    if any(e > 1 for e in factors.values()):
        return 0
    return -1 if len(factors) % 2 else 1


is_perfect = lambda n: n > 1 and divisor_sum(n) - n == n
is_abundant = lambda n: divisor_sum(n) - n > n
is_deficient = lambda n: divisor_sum(n) - n < n
is_perfect_square = lambda n: n >= 0 and math.isqrt(n) ** 2 == n
is_power_of_two = lambda n: n > 0 and n & (n - 1) == 0
is_palindrome_number = lambda n: str(abs(n)) == str(abs(n))[::-1]
digit_sum = lambda n: sum(int(d) for d in str(abs(n)))
count_digits = lambda n: len(str(abs(n)))
reverse_digits = lambda n: int(str(abs(n))[::-1]) * (1 if n >= 0 else -1)
digital_root = lambda n: 0 if n == 0 else 1 + (abs(n) - 1) % 9
is_armstrong = lambda n: n == sum(int(d) ** len(str(n)) for d in str(n))


def is_perfect_cube(n):
    """True if n is a whole number cubed (negative numbers allowed)."""
    m = abs(n)
    c = round(m ** (1 / 3))
    return any((c + shift) ** 3 == m for shift in (-1, 0, 1))


def collatz_sequence(n):
    """The 3n+1 sequence starting at n until it reaches 1."""
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


collatz_steps = lambda n: len(collatz_sequence(n)) - 1


def to_base(n, base):
    """Integer n written in the given base (2-36), e.g. (255, 16) -> 'ff'."""
    if not 2 <= base <= 36:
        raise ValueError("base must be between 2 and 36")
    if n == 0:
        return "0"
    symbols = "0123456789abcdefghijklmnopqrstuvwxyz"
    prefix = "-" if n < 0 else ""
    n = abs(n)
    out = []
    while n:
        n, r = divmod(n, base)
        out.append(symbols[r])
    return prefix + "".join(reversed(out))


from_base = lambda text, base: int(text, base)
to_binary = lambda n: to_base(n, 2)
to_octal = lambda n: to_base(n, 8)
to_hexadecimal = lambda n: to_base(n, 16)
from_binary = lambda text: int(text, 2)
from_octal = lambda text: int(text, 8)
from_hexadecimal = lambda text: int(text, 16)

# --- Sequences & Series ---
arithmetic_nth_term = lambda first, difference, n: first + (n - 1) * difference
arithmetic_sum = lambda first, difference, n: n * (2 * first + (n - 1) * difference) / 2
arithmetic_sum_first_last = lambda first, last, n: n * (first + last) / 2
arithmetic_term_count = lambda first, last, difference: (last - first) / difference + 1
arithmetic_mean_between = lambda a, b: (a + b) / 2
geometric_nth_term = lambda first, ratio_, n: first * ratio_ ** (n - 1)
geometric_sum = lambda first, ratio_, n: first * n if ratio_ == 1 else first * (1 - ratio_ ** n) / (1 - ratio_)
geometric_mean_between = lambda a, b: math.sqrt(a * b)
harmonic_mean_between = lambda a, b: 2 * a * b / (a + b)
harmonic_number = lambda n: sum(1 / k for k in range(1, n + 1))
sum_natural = lambda n: n * (n + 1) // 2
sum_squares = lambda n: n * (n + 1) * (2 * n + 1) // 6
sum_cubes = lambda n: (n * (n + 1) // 2) ** 2
sum_fourth_powers = lambda n: n * (n + 1) * (2 * n + 1) * (3 * n * n + 3 * n - 1) // 30
sum_odd_numbers = lambda n: n * n
sum_even_numbers = lambda n: n * (n + 1)
sum_of_powers = lambda n, p: sum(k ** p for k in range(1, n + 1))
triangular_number = lambda n: n * (n + 1) // 2
pentagonal_number = lambda n: n * (3 * n - 1) // 2
hexagonal_number = lambda n: n * (2 * n - 1)
polygonal_number = lambda sides, n: ((sides - 2) * n * n - (sides - 4) * n) // 2
tetrahedral_number = lambda n: n * (n + 1) * (n + 2) // 6
square_pyramidal_number = lambda n: n * (n + 1) * (2 * n + 1) // 6
pronic_number = lambda n: n * (n + 1)
mersenne_number = lambda p: 2 ** p - 1
fermat_number = lambda n: 2 ** (2 ** n) + 1
catalan_number = lambda n: math.comb(2 * n, n) // (n + 1)
is_triangular_number = lambda n: n >= 0 and is_perfect_square(8 * n + 1)


def geometric_sum_infinite(first, ratio_):
    """Sum of an infinite geometric series (only when |ratio| < 1)."""
    if abs(ratio_) >= 1:
        raise ValueError("the series only converges when |ratio| < 1")
    return first / (1 - ratio_)


def fibonacci(n):
    """n-th Fibonacci number (F0 = 0, F1 = 1), exact, using fast doubling."""
    if n < 0:
        raise ValueError("n must be >= 0")

    def doubling(k):
        if k == 0:
            return 0, 1
        a, b = doubling(k // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        return (d, c + d) if k % 2 else (c, d)

    return doubling(n)[0]


fibonacci_binet = lambda n: round(PHI ** n / SQRT5)
fibonacci_sequence = lambda count: [fibonacci(i) for i in range(count)]
is_fibonacci = lambda n: n >= 0 and (is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4))


def lucas_number(n):
    """n-th Lucas number (L0 = 2, L1 = 1)."""
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# --- Combinatorics ---
factorial = lambda n: math.factorial(n)
permutations = lambda n, r: math.perm(n, r)
combinations = lambda n, r: math.comb(n, r)
nPr = permutations
nCr = combinations
permutations_repetition = lambda n, r: n ** r
combinations_repetition = lambda n, r: math.comb(n + r - 1, r)
circular_permutations = lambda n: math.factorial(n - 1)
handshakes = lambda n: n * (n - 1) // 2
pigeonhole_minimum = lambda items, boxes: -(-items // boxes)
inclusion_exclusion_two = lambda a, b, a_and_b: a + b - a_and_b
inclusion_exclusion_three = lambda a, b, c, ab, ac, bc, abc: a + b + c - ab - ac - bc + abc
binomial_expansion_term = lambda n, k, a, b: math.comb(n, k) * a ** (n - k) * b ** k


def double_factorial(n):
    """n!! = n * (n-2) * (n-4) * ..."""
    result = 1
    while n > 1:
        result *= n
        n -= 2
    return result


def multinomial(*counts):
    """(k1 + k2 + ...)! / (k1! * k2! * ...) -- also arrangements of a word with repeated letters."""
    result = math.factorial(sum(counts))
    for k in counts:
        result //= math.factorial(k)
    return result


def derangements(n):
    """Ways to shuffle n items so that none stays in its place (subfactorial)."""
    a, b = 1, 0
    if n == 0:
        return 1
    for k in range(2, n + 1):
        a, b = b, (k - 1) * (a + b)
    return b


def stirling_second(n, k):
    """Ways to split n items into k non-empty groups."""
    return sum((-1) ** (k - j) * math.comb(k, j) * j ** n for j in range(k + 1)) // math.factorial(k)


def stirling_first(n, k):
    """Unsigned Stirling number of the first kind: permutations of n items with k cycles."""
    table = [[0] * (k + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            table[i][j] = table[i - 1][j - 1] + (i - 1) * table[i - 1][j]
    return table[n][k]


def bell_number(n):
    """Number of ways to partition a set of n items."""
    row = [1]
    for _ in range(n):
        new = [row[-1]]
        for x in row:
            new.append(new[-1] + x)
        row = new
    return row[0]


def partition_number(n):
    """Number of ways to write n as a sum of positive integers (order ignored)."""
    p = [1] + [0] * n
    for i in range(1, n + 1):
        k = 1
        total = 0
        while True:
            g1 = k * (3 * k - 1) // 2
            if g1 > i:
                break
            s = 1 if k % 2 else -1
            total += s * p[i - g1]
            g2 = k * (3 * k + 1) // 2
            if g2 <= i:
                total += s * p[i - g2]
            k += 1
        p[i] = total
    return p[n]


def necklace_count(beads, colours):
    """Distinct necklaces of `beads` beads in `colours` colours (rotations count as the same)."""
    return sum(euler_totient(d) * colours ** (beads // d) for d in divisors(beads)) // beads


pascal_row = lambda n: [math.comb(n, k) for k in range(n + 1)]
pascal_triangle = lambda rows: [pascal_row(n) for n in range(rows)]

# --- Linear & Quadratic Algebra ---
linear_solve = lambda a, b: -b / a                     # ax + b = 0
quadratic_discriminant = lambda a, b, c: b * b - 4 * a * c
quadratic_axis_of_symmetry = lambda a, b, c: -b / (2 * a)
quadratic_vertex = lambda a, b, c: (-b / (2 * a), c - b * b / (4 * a))
quadratic_sum_of_roots = lambda a, b, c: -b / a
quadratic_product_of_roots = lambda a, b, c: c / a
quadratic_from_roots = lambda r1, r2: (1, -(r1 + r2), r1 * r2)
quadratic_complete_square = lambda a, b, c: (a, -b / (2 * a), c - b * b / (4 * a))   # a(x - h)^2 + k -> (a, h, k)
quadratic_extreme_value = lambda a, b, c: c - b * b / (4 * a)


def quadratic_roots(a, b, c):
    """Roots of ax^2 + bx + c = 0. Floats, or complex numbers when the discriminant is negative."""
    if a == 0:
        raise ValueError("a must not be 0 (that is linear, use linear_solve)")
    d = b * b - 4 * a * c
    if d >= 0:
        s = math.sqrt(d)
        q = -0.5 * (b + math.copysign(s, b))
        if q == 0:
            return 0.0, 0.0
        return tuple(sorted((q / a, c / q)))
    s = math.sqrt(-d)
    return complex(-b / (2 * a), s / (2 * a)), complex(-b / (2 * a), -s / (2 * a))


def solve_2x2(a1, b1, c1, a2, b2, c2):
    """Solves a1*x + b1*y = c1 and a2*x + b2*y = c2 with Cramer's rule."""
    det = a1 * b2 - a2 * b1
    if det == 0:
        raise ValueError("no unique solution (lines are parallel or identical)")
    return (c1 * b2 - c2 * b1) / det, (a1 * c2 - a2 * c1) / det


def cubic_roots(a, b, c, d):
    """Roots of ax^3 + bx^2 + cx + d = 0 (Cardano / trigonometric method); complex where needed."""
    if a == 0:
        raise ValueError("a must not be 0 (use quadratic_roots)")
    b, c, d = b / a, c / a, d / a
    p = c - b * b / 3
    q = 2 * b ** 3 / 27 - b * c / 3 + d
    shift = -b / 3
    disc = (q / 2) ** 2 + (p / 3) ** 3
    scale = max((q / 2) ** 2, abs((p / 3) ** 3), 1e-300)
    real_cbrt = lambda v: math.copysign(abs(v) ** (1 / 3), v)
    if abs(disc) <= 1e-12 * scale:
        if abs(p) < 1e-14 and abs(q) < 1e-14:
            return shift, shift, shift
        u = real_cbrt(-q / 2)
        return tuple(sorted((2 * u + shift, -u + shift, -u + shift)))
    if disc > 0:
        s = math.sqrt(disc)
        u = real_cbrt(-q / 2 + s)
        v = real_cbrt(-q / 2 - s)
        real = u + v + shift
        re = -(u + v) / 2 + shift
        im = SQRT3 / 2 * (u - v)
        return real, complex(re, im), complex(re, -im)
    r = 2 * math.sqrt(-p / 3)
    arg = max(-1.0, min(1.0, 3 * q / (2 * p) * math.sqrt(-3 / p)))
    phi = math.acos(arg) / 3
    return tuple(sorted(r * math.cos(phi - TAU * k / 3) + shift for k in range(3)))


cubic_discriminant = lambda a, b, c, d: 18 * a * b * c * d - 4 * b ** 3 * d + b * b * c * c - 4 * a * c ** 3 - 27 * a * a * d * d

# --- Polynomials (coefficients run from the highest power down: [1, 0, -4] is x^2 - 4) ---
def poly_eval(coefficients, x):
    """Value of a polynomial at x (Horner's method)."""
    result = 0
    for c in coefficients:
        result = result * x + c
    return result


def poly_derivative(coefficients):
    """Coefficients of the derivative."""
    n = len(coefficients) - 1
    if n <= 0:
        return [0]
    return [c * (n - i) for i, c in enumerate(coefficients[:-1])]


def poly_integral(coefficients, constant=0):
    """Coefficients of the antiderivative (plus the constant of integration)."""
    n = len(coefficients)
    return [c / (n - i) for i, c in enumerate(coefficients)] + [constant]


poly_definite_integral = lambda coefficients, a, b: poly_eval(poly_integral(coefficients), b) - poly_eval(poly_integral(coefficients), a)
poly_degree = lambda coefficients: len(coefficients) - 1


def poly_add(p, q):
    """Adds two polynomials."""
    n = max(len(p), len(q))
    p = [0] * (n - len(p)) + list(p)
    q = [0] * (n - len(q)) + list(q)
    return [x + y for x, y in zip(p, q)]


def poly_multiply(p, q):
    """Multiplies two polynomials."""
    result = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            result[i + j] += x * y
    return result


def poly_divide(numerator, denominator):
    """Polynomial long division -> (quotient, remainder)."""
    num = list(numerator)
    if denominator[0] == 0:
        raise ZeroDivisionError("leading coefficient of the divisor is 0")
    quotient = []
    while len(num) >= len(denominator):
        factor = num[0] / denominator[0]
        quotient.append(factor)
        for i, d in enumerate(denominator):
            num[i] -= factor * d
        num.pop(0)
    return quotient or [0], num or [0]


def synthetic_division(coefficients, r):
    """Divides by (x - r) -> (quotient, remainder). The remainder equals the value at r."""
    row = [coefficients[0]]
    for c in coefficients[1:]:
        row.append(c + row[-1] * r)
    return row[:-1], row[-1]


def poly_from_roots(roots):
    """Coefficients of the monic polynomial with the given roots."""
    result = [1]
    for r in roots:
        result = poly_multiply(result, [1, -r])
    return result


def polynomial_roots(coefficients, iterations=2000, tolerance=1e-14):
    """All roots (real and complex) of any polynomial, by the Durand-Kerner method."""
    coeffs = list(coefficients)
    while coeffs and coeffs[0] == 0:
        coeffs.pop(0)
    n = len(coeffs) - 1
    if n < 1:
        return []
    monic = [c / coeffs[0] for c in coeffs]
    radius = max(abs(monic[k]) ** (1 / k) for k in range(1, n + 1))
    if radius == 0:
        return [0.0] * n
    roots = [radius * complex(math.cos(TAU * k / n + 0.5), math.sin(TAU * k / n + 0.5)) for k in range(n)]
    for _ in range(iterations):
        biggest = 0.0
        for i in range(n):
            denominator = 1
            for j in range(n):
                if j != i:
                    denominator *= roots[i] - roots[j]
            delta = poly_eval(monic, roots[i]) / denominator
            roots[i] -= delta
            biggest = max(biggest, abs(delta))
        if biggest < tolerance:
            break
    cleaned = []
    for z in roots:
        if abs(z.imag) < 1e-8 * max(1.0, abs(z.real)):
            cleaned.append(z.real)
        else:
            cleaned.append(z)
    return sorted(cleaned, key=lambda z: (z.real, z.imag) if isinstance(z, complex) else (z, 0))


quartic_roots = lambda a, b, c, d, e: polynomial_roots([a, b, c, d, e])
cauchy_root_bound = lambda coefficients: 1 + max(abs(c / coefficients[0]) for c in coefficients[1:])
descartes_sign_changes = lambda coefficients: sum(1 for x, y in zip([c for c in coefficients if c], [c for c in coefficients if c][1:]) if x * y < 0)


def rational_root_candidates(coefficients):
    """Possible rational roots +-p/q (integer coefficients) from the rational root theorem."""
    coeffs = list(coefficients)
    found = set()
    while coeffs and coeffs[-1] == 0:
        coeffs.pop()
        found.add(0.0)
    if len(coeffs) > 1:
        for p in divisors(abs(int(coeffs[-1]))):
            for q in divisors(abs(int(coeffs[0]))):
                found.add(p / q)
                found.add(-p / q)
    return sorted(found)


# --- Interpolation ---
linear_interpolation = lambda x, x0, y0, x1, y1: y0 + (x - x0) * (y1 - y0) / (x1 - x0)


def lagrange_interpolation(xs, ys, x):
    """Value at x of the polynomial passing through all the points (xs[i], ys[i])."""
    total = 0.0
    for i in range(len(xs)):
        term = ys[i]
        for j in range(len(xs)):
            if i != j:
                term *= (x - xs[j]) / (xs[i] - xs[j])
        total += term
    return total


def bilinear_interpolation(x, y, x1, x2, y1, y2, q11, q12, q21, q22):
    """Interpolates between corner values q11=f(x1,y1), q12=f(x1,y2), q21=f(x2,y1), q22=f(x2,y2)."""
    return (q11 * (x2 - x) * (y2 - y) + q21 * (x - x1) * (y2 - y) + q12 * (x2 - x) * (y - y1) + q22 * (x - x1) * (y - y1)) / ((x2 - x1) * (y2 - y1))


# --- Derivatives (numerical) ---
def derivative(f, x, h=1e-3):
    """First derivative of f at x (five-point stencil)."""
    return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)


def second_derivative(f, x, h=1e-3):
    """Second derivative of f at x (five-point stencil)."""
    return (-f(x + 2 * h) + 16 * f(x + h) - 30 * f(x) + 16 * f(x - h) - f(x - 2 * h)) / (12 * h * h)


def partial_derivative(f, point, index, h=1e-3):
    """Partial derivative of f(x, y, ...) with respect to the variable at `index`."""
    def shifted(k):
        p = list(point)
        p[index] += k * h
        return f(*p)
    return (-shifted(2) + 8 * shifted(1) - 8 * shifted(-1) + shifted(-2)) / (12 * h)


gradient = lambda f, point, h=1e-3: [partial_derivative(f, point, i, h) for i in range(len(point))]
directional_derivative = lambda f, point, direction, h=1e-3: sum(g * d for g, d in zip(gradient(f, point, h), direction)) / math.sqrt(sum(d * d for d in direction))
curvature = lambda f, x: abs(second_derivative(f, x)) / (1 + derivative(f, x) ** 2) ** 1.5
tangent_line = lambda f, x0: (derivative(f, x0), f(x0) - derivative(f, x0) * x0)          # (slope, intercept)
normal_line = lambda f, x0: (-1 / derivative(f, x0), f(x0) + x0 / derivative(f, x0))      # (slope, intercept)
limit_numeric = lambda f, x0, h=1e-6: (f(x0 + h) + f(x0 - h)) / 2


def hessian(f, point, h=1e-3):
    """Matrix of second partial derivatives of f at `point`."""
    n = len(point)

    def value(shifts):
        p = list(point)
        for index, k in shifts:
            p[index] += k * h
        return f(*p)

    result = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                result[i][j] = (value([(i, 1)]) - 2 * f(*point) + value([(i, -1)])) / (h * h)
            else:
                result[i][j] = (value([(i, 1), (j, 1)]) - value([(i, 1), (j, -1)]) - value([(i, -1), (j, 1)]) + value([(i, -1), (j, -1)])) / (4 * h * h)
    return result


# --- Integrals (numerical) ---
def integral_trapezoid(f, a, b, n=1000):
    """Trapezoid rule."""
    h = (b - a) / n
    total = (f(a) + f(b)) / 2
    for i in range(1, n):
        total += f(a + i * h)
    return total * h


def integral_midpoint(f, a, b, n=1000):
    """Midpoint rule."""
    h = (b - a) / n
    return h * sum(f(a + (i + 0.5) * h) for i in range(n))


def integral_simpson(f, a, b, n=1000):
    """Simpson's 1/3 rule (n is made even)."""
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * f(a + i * h)
    return total * h / 3


def integral_adaptive(f, a, b, tolerance=1e-10, max_depth=40):
    """Adaptive Simpson integration to the requested tolerance."""
    def simpson(fa, fm, fb, left, right):
        return (right - left) / 6 * (fa + 4 * fm + fb)

    def recurse(left, right, fa, fm, fb, whole, tol, depth):
        mid = (left + right) / 2
        flm, frm = f((left + mid) / 2), f((mid + right) / 2)
        half_left = simpson(fa, flm, fm, left, mid)
        half_right = simpson(fm, frm, fb, mid, right)
        if depth <= 0 or abs(half_left + half_right - whole) <= 15 * tol:
            return half_left + half_right + (half_left + half_right - whole) / 15
        return (recurse(left, mid, fa, flm, fm, half_left, tol / 2, depth - 1)
                + recurse(mid, right, fm, frm, fb, half_right, tol / 2, depth - 1))

    fa, fb, fm = f(a), f(b), f((a + b) / 2)
    return recurse(a, b, fa, fm, fb, simpson(fa, fm, fb, a, b), tolerance, max_depth)


def integral_gauss(f, a, b, panels=50):
    """Composite 5-point Gauss-Legendre quadrature (very accurate for smooth functions)."""
    nodes = (0.0, -0.5384693101056831, 0.5384693101056831, -0.9061798459386640, 0.9061798459386640)
    weights = (0.5688888888888889, 0.4786286704993665, 0.4786286704993665, 0.2369268850561891, 0.2369268850561891)
    width = (b - a) / panels
    half = width / 2
    total = 0.0
    for p in range(panels):
        mid = a + (p + 0.5) * width
        total += half * sum(w * f(mid + half * x) for x, w in zip(nodes, weights))
    return total


integral_to_infinity = lambda f, a, panels=200: integral_gauss(lambda t: f(a + t / (1 - t)) / (1 - t) ** 2, 0, 1, panels)
integral_real_line = lambda f, panels=400: integral_gauss(lambda t: f(t / (1 - t * t)) * (1 + t * t) / (1 - t * t) ** 2, -1, 1, panels)
double_integral = lambda f, x0, x1, y0, y1, n=20: integral_gauss(lambda x: integral_gauss(lambda y: f(x, y), y0, y1, n), x0, x1, n)
average_value = lambda f, a, b, n=2000: integral_simpson(f, a, b, n) / (b - a)
arc_length_curve = lambda f, a, b, n=2000: integral_simpson(lambda x: math.sqrt(1 + derivative(f, x) ** 2), a, b, n)
surface_area_revolution = lambda f, a, b, n=2000: 2 * PI * integral_simpson(lambda x: f(x) * math.sqrt(1 + derivative(f, x) ** 2), a, b, n)
volume_revolution_disk = lambda f, a, b, n=2000: PI * integral_simpson(lambda x: f(x) ** 2, a, b, n)
volume_revolution_shell = lambda f, a, b, n=2000: 2 * PI * integral_simpson(lambda x: x * f(x), a, b, n)
area_between_curves = lambda f, g, a, b, n=2000: integral_simpson(lambda x: abs(f(x) - g(x)), a, b, n)

# --- Root Finding & Optimisation ---
def newton_raphson(f, x0, df=None, tolerance=1e-12, max_iterations=100):
    """Finds a root of f near x0 (df is optional, otherwise it is estimated)."""
    x = x0
    for _ in range(max_iterations):
        slope = df(x) if df else derivative(f, x)
        if slope == 0:
            raise ZeroDivisionError("derivative is 0 here, try another starting point")
        step = f(x) / slope
        x -= step
        if abs(step) < tolerance:
            return x
    raise ArithmeticError("Newton-Raphson did not converge")


def bisection(f, a, b, tolerance=1e-12, max_iterations=200):
    """Finds a root of f between a and b (f(a) and f(b) must have opposite signs)."""
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    for _ in range(max_iterations):
        m = (a + b) / 2
        fm = f(m)
        if fm == 0 or (b - a) / 2 < tolerance:
            return m
        if fa * fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a + b) / 2


def secant_method(f, x0, x1, tolerance=1e-12, max_iterations=100):
    """Finds a root of f from two starting guesses."""
    for _ in range(max_iterations):
        f0, f1 = f(x0), f(x1)
        if f1 == f0:
            raise ZeroDivisionError("flat secant line")
        x0, x1 = x1, x1 - f1 * (x1 - x0) / (f1 - f0)
        if abs(x1 - x0) < tolerance:
            return x1
    raise ArithmeticError("secant method did not converge")


def fixed_point_iteration(g, x0, tolerance=1e-12, max_iterations=1000):
    """Solves x = g(x) by repeating x -> g(x)."""
    x = x0
    for _ in range(max_iterations):
        new = g(x)
        if abs(new - x) < tolerance:
            return new
        x = new
    raise ArithmeticError("fixed point iteration did not converge")


def golden_section_minimum(f, a, b, tolerance=1e-10):
    """x that minimises a single-valley function f on [a, b]."""
    inv = 1 / PHI
    c, d = b - (b - a) * inv, a + (b - a) * inv
    while abs(b - a) > tolerance:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c, d = b - (b - a) * inv, a + (b - a) * inv
    return (a + b) / 2


# --- Differential Equations ---
def euler_method(f, x0, y0, h, steps):
    """Solves y' = f(x, y) with Euler's method -> list of (x, y)."""
    points = [(x0, y0)]
    x, y = x0, y0
    for _ in range(steps):
        y += h * f(x, y)
        x += h
        points.append((x, y))
    return points


def heun_method(f, x0, y0, h, steps):
    """Solves y' = f(x, y) with Heun's (improved Euler) method -> list of (x, y)."""
    points = [(x0, y0)]
    x, y = x0, y0
    for _ in range(steps):
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        y += h / 2 * (k1 + k2)
        x += h
        points.append((x, y))
    return points


def runge_kutta4(f, x0, y0, h, steps):
    """Solves y' = f(x, y) with the classic 4th-order Runge-Kutta method -> list of (x, y)."""
    points = [(x0, y0)]
    x, y = x0, y0
    for _ in range(steps):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
        y += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
        points.append((x, y))
    return points


# --- Series (Taylor / Maclaurin) ---
series_exp = lambda x, terms=30: sum(x ** k / math.factorial(k) for k in range(terms))
series_sin = lambda x, terms=15: sum((-1) ** k * x ** (2 * k + 1) / math.factorial(2 * k + 1) for k in range(terms))
series_cos = lambda x, terms=15: sum((-1) ** k * x ** (2 * k) / math.factorial(2 * k) for k in range(terms))
series_sinh = lambda x, terms=15: sum(x ** (2 * k + 1) / math.factorial(2 * k + 1) for k in range(terms))
series_cosh = lambda x, terms=15: sum(x ** (2 * k) / math.factorial(2 * k) for k in range(terms))
series_ln1p = lambda x, terms=200: sum((-1) ** (k + 1) * x ** k / k for k in range(1, terms + 1))      # ln(1 + x), |x| < 1
series_atan = lambda x, terms=200: sum((-1) ** k * x ** (2 * k + 1) / (2 * k + 1) for k in range(terms))   # |x| <= 1
series_geometric = lambda x, terms=100: sum(x ** k for k in range(terms))                                # 1/(1-x), |x| < 1
series_binomial = lambda x, alpha, terms=60: sum(math.prod(alpha - i for i in range(k)) / math.factorial(k) * x ** k for k in range(terms))   # (1+x)^alpha, |x| < 1


def fourier_coefficients(f, period, n, samples=2000):
    """(a_n, b_n) Fourier coefficients of a periodic function f over one period starting at 0."""
    w = TAU * n / period
    a_n = 2 / period * integral_simpson(lambda x: f(x) * math.cos(w * x), 0, period, samples)
    b_n = 2 / period * integral_simpson(lambda x: f(x) * math.sin(w * x), 0, period, samples)
    return a_n, b_n


def discrete_fourier_transform(samples):
    """Discrete Fourier transform of a list of numbers -> list of complex numbers."""
    n = len(samples)
    result = []
    for k in range(n):
        re = sum(x * math.cos(TAU * k * j / n) for j, x in enumerate(samples))
        im = -sum(x * math.sin(TAU * k * j / n) for j, x in enumerate(samples))
        result.append(complex(re, im))
    return result


def inverse_discrete_fourier_transform(spectrum):
    """Inverse discrete Fourier transform -> list of real numbers."""
    n = len(spectrum)
    return [sum(z.real * math.cos(TAU * k * j / n) - z.imag * math.sin(TAU * k * j / n) for k, z in enumerate(spectrum)) / n for j in range(n)]

# --- Angle Units ---
deg_to_rad = lambda d: math.radians(d)
rad_to_deg = lambda r: math.degrees(r)
deg_to_grad = lambda d: d * 10 / 9
grad_to_deg = lambda g: g * 9 / 10
rad_to_grad = lambda r: r * 200 / PI
grad_to_rad = lambda g: g * PI / 200
normalize_angle_deg = lambda a: a % 360
angle_difference_deg = lambda a, b: (b - a + 180) % 360 - 180


def deg_to_dms(degrees):
    """Decimal degrees -> (degrees, minutes, seconds)."""
    negative = degrees < 0
    d = abs(degrees)
    whole = int(d)
    minutes_full = (d - whole) * 60
    minutes = int(minutes_full)
    seconds = (minutes_full - minutes) * 60
    return (-whole if negative else whole), minutes, seconds


dms_to_deg = lambda d, m, s: (abs(d) + m / 60 + s / 3600) * (-1 if d < 0 else 1)

# --- Trigonometry (degrees) ---


def sin_deg(x):
    """Sine of an angle in degrees (exact at multiples of 90)."""
    exact = {0: 0.0, 90: 1.0, 180: 0.0, 270: -1.0}
    r = x % 360
    return exact[r] if r in exact else math.sin(math.radians(x))


def cos_deg(x):
    """Cosine of an angle in degrees (exact at multiples of 90)."""
    exact = {0: 1.0, 90: 0.0, 180: -1.0, 270: 0.0}
    r = x % 360
    return exact[r] if r in exact else math.cos(math.radians(x))


def tan_deg(x):
    """Tangent of an angle in degrees (exact at multiples of 90, undefined at 90 and 270)."""
    r = x % 180
    if r == 90:
        raise ValueError("tan is undefined at 90 degrees (and 270, 450, ...)")
    if r == 0:
        return 0.0
    return math.tan(math.radians(x))


asin_deg = lambda x: math.degrees(math.asin(x))
acos_deg = lambda x: math.degrees(math.acos(x))
atan_deg = lambda x: math.degrees(math.atan(x))
atan2_deg = lambda y, x: math.degrees(math.atan2(y, x))
sec_deg = lambda x: 1 / cos_deg(x)
csc_deg = lambda x: 1 / sin_deg(x)
cot_deg = lambda x: 1 / tan_deg(x)
asec_deg = lambda x: acos_deg(1 / x)
acsc_deg = lambda x: asin_deg(1 / x)
acot_deg = lambda x: atan2_deg(1, x)

# --- Trigonometry (radians), reciprocal and hyperbolic ---
sec = lambda x: 1 / math.cos(x)
csc = lambda x: 1 / math.sin(x)
cot = lambda x: 1 / math.tan(x)
asec = lambda x: math.acos(1 / x)
acsc = lambda x: math.asin(1 / x)
acot = lambda x: math.atan2(1, x)
sinh = lambda x: math.sinh(x)
cosh = lambda x: math.cosh(x)
tanh = lambda x: math.tanh(x)
asinh = lambda x: math.asinh(x)
acosh = lambda x: math.acosh(x)
atanh = lambda x: math.atanh(x)
sech = lambda x: 1 / math.cosh(x)
csch = lambda x: 1 / math.sinh(x)
coth = lambda x: 1 / math.tanh(x)
asech = lambda x: math.acosh(1 / x)
acsch = lambda x: math.asinh(1 / x)
acoth = lambda x: math.atanh(1 / x)
unit_circle_point = lambda angle: (cos_deg(angle), sin_deg(angle))

# --- Trigonometric Identities (angles in degrees) ---
sin_sum = lambda a, b: sin_deg(a) * cos_deg(b) + cos_deg(a) * sin_deg(b)
sin_difference = lambda a, b: sin_deg(a) * cos_deg(b) - cos_deg(a) * sin_deg(b)
cos_sum = lambda a, b: cos_deg(a) * cos_deg(b) - sin_deg(a) * sin_deg(b)
cos_difference = lambda a, b: cos_deg(a) * cos_deg(b) + sin_deg(a) * sin_deg(b)
tan_sum = lambda a, b: (tan_deg(a) + tan_deg(b)) / (1 - tan_deg(a) * tan_deg(b))
tan_difference = lambda a, b: (tan_deg(a) - tan_deg(b)) / (1 + tan_deg(a) * tan_deg(b))
sin_double = lambda a: 2 * sin_deg(a) * cos_deg(a)
cos_double = lambda a: cos_deg(a) ** 2 - sin_deg(a) ** 2
tan_double = lambda a: 2 * tan_deg(a) / (1 - tan_deg(a) ** 2)
sin_triple = lambda a: 3 * sin_deg(a) - 4 * sin_deg(a) ** 3
cos_triple = lambda a: 4 * cos_deg(a) ** 3 - 3 * cos_deg(a)
sin_half = lambda a, sign_=1: sign_ * math.sqrt((1 - cos_deg(a)) / 2)      # sign_ = +1 or -1 depending on the quadrant of a/2
cos_half = lambda a, sign_=1: sign_ * math.sqrt((1 + cos_deg(a)) / 2)
tan_half = lambda a: sin_deg(a) / (1 + cos_deg(a))
sin_squared = lambda a: (1 - cos_deg(2 * a)) / 2
cos_squared = lambda a: (1 + cos_deg(2 * a)) / 2
product_sin_cos = lambda a, b: (sin_deg(a + b) + sin_deg(a - b)) / 2        # sin a * cos b
product_cos_cos = lambda a, b: (cos_deg(a - b) + cos_deg(a + b)) / 2        # cos a * cos b
product_sin_sin = lambda a, b: (cos_deg(a - b) - cos_deg(a + b)) / 2        # sin a * sin b
sum_sin_sin = lambda a, b: 2 * sin_deg((a + b) / 2) * cos_deg((a - b) / 2)  # sin a + sin b
sum_cos_cos = lambda a, b: 2 * cos_deg((a + b) / 2) * cos_deg((a - b) / 2)  # cos a + cos b
auxiliary_amplitude = lambda a, b: math.hypot(a, b)                         # a sin x + b cos x = R sin(x + phi)
auxiliary_phase = lambda a, b: atan2_deg(b, a)

# --- Right Triangle Trig (SOH-CAH-TOA) ---
trig_opposite = lambda hypotenuse, angle: hypotenuse * sin_deg(angle)
trig_adjacent = lambda hypotenuse, angle: hypotenuse * cos_deg(angle)
trig_opposite_from_adjacent = lambda adjacent, angle: adjacent * tan_deg(angle)
trig_adjacent_from_opposite = lambda opposite, angle: opposite / tan_deg(angle)
trig_hypotenuse_from_opposite = lambda opposite, angle: opposite / sin_deg(angle)
trig_hypotenuse_from_adjacent = lambda adjacent, angle: adjacent / cos_deg(angle)
trig_angle_from_opposite_adjacent = lambda opposite, adjacent: atan2_deg(opposite, adjacent)
trig_angle_from_opposite_hypotenuse = lambda opposite, hypotenuse: asin_deg(opposite / hypotenuse)
trig_angle_from_adjacent_hypotenuse = lambda adjacent, hypotenuse: acos_deg(adjacent / hypotenuse)
slope_to_angle = lambda slope: atan_deg(slope)
angle_to_slope = lambda angle: tan_deg(angle)

# --- Waves ---
wave_value = lambda amplitude, angular_frequency, phase, offset, x: amplitude * math.sin(angular_frequency * x + phase) + offset
wave_period = lambda angular_frequency: TAU / abs(angular_frequency)
wave_frequency = lambda angular_frequency: abs(angular_frequency) / TAU
wave_phase_shift = lambda c, b: -c / b
wave_angular_frequency = lambda period: TAU / period

# --- Coordinate Systems ---
polar_to_cartesian = lambda r, theta: (r * cos_deg(theta), r * sin_deg(theta))
cartesian_to_polar = lambda x, y: (math.hypot(x, y), atan2_deg(y, x))
cylindrical_to_cartesian = lambda r, theta, z: (r * cos_deg(theta), r * sin_deg(theta), z)
cartesian_to_cylindrical = lambda x, y, z: (math.hypot(x, y), atan2_deg(y, x), z)
# Spherical: r, theta = angle down from the +z axis, phi = angle around the z axis (degrees)
spherical_to_cartesian = lambda r, theta, phi: (r * sin_deg(theta) * cos_deg(phi), r * sin_deg(theta) * sin_deg(phi), r * cos_deg(theta))


def cartesian_to_spherical(x, y, z):
    """(x, y, z) -> (r, theta, phi) with theta measured from the +z axis, in degrees."""
    r = math.sqrt(x * x + y * y + z * z)
    if r == 0:
        return 0.0, 0.0, 0.0
    return r, acos_deg(z / r), atan2_deg(y, x)


def haversine_distance(lat1, lon1, lat2, lon2, radius=6371.0088):
    """Great-circle distance between two lat/lon points (degrees). Default radius = Earth in km."""
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * radius * math.asin(min(1.0, math.sqrt(h)))


def initial_bearing(lat1, lon1, lat2, lon2):
    """Compass bearing (degrees, 0 = north) to head from point 1 towards point 2."""
    p1, p2, dl = math.radians(lat1), math.radians(lat2), math.radians(lon2 - lon1)
    y = math.sin(dl) * math.cos(p2)
    x = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl)
    return (math.degrees(math.atan2(y, x)) + 360) % 360


def destination_point(lat, lon, bearing, distance, radius=6371.0088):
    """Lat/lon reached by travelling `distance` from a start point along a bearing (degrees)."""
    p1, l1, b = math.radians(lat), math.radians(lon), math.radians(bearing)
    d = distance / radius
    p2 = math.asin(math.sin(p1) * math.cos(d) + math.cos(p1) * math.sin(d) * math.cos(b))
    l2 = l1 + math.atan2(math.sin(b) * math.sin(d) * math.cos(p1), math.cos(d) - math.sin(p1) * math.sin(p2))
    return math.degrees(p2), (math.degrees(l2) + 540) % 360 - 180


# --- Squares, Rectangles & Friends ---
square_area_s = lambda s: s ** 2
square_perimeter_s = lambda s: 4 * s
square_diagonal_s = lambda s: s * SQRT2
square_side_d = lambda d: d / SQRT2
square_area_d = lambda d: d ** 2 / 2
square_inradius_s = lambda s: s / 2
square_circumradius_s = lambda s: s / SQRT2
rectangle_area = lambda length, width: length * width
rectangle_perimeter = lambda length, width: 2 * (length + width)
rectangle_diagonal = lambda length, width: math.hypot(length, width)
parallelogram_area_bh = lambda base, height: base * height
parallelogram_area_sides_angle = lambda a, b, theta: a * b * sin_deg(theta)
parallelogram_perimeter = lambda a, b: 2 * (a + b)
parallelogram_diagonals = lambda a, b, theta: (math.sqrt(a * a + b * b + 2 * a * b * cos_deg(theta)), math.sqrt(a * a + b * b - 2 * a * b * cos_deg(theta)))
rhombus_area_diagonals = lambda d1, d2: d1 * d2 / 2
rhombus_area_side_angle = lambda s, theta: s * s * sin_deg(theta)
rhombus_side_from_diagonals = lambda d1, d2: math.hypot(d1, d2) / 2
rhombus_perimeter = lambda s: 4 * s
rhombus_inradius = lambda d1, d2: d1 * d2 / (2 * math.hypot(d1, d2))
trapezoid_area = lambda a, b, h: (a + b) / 2 * h
trapezoid_median = lambda a, b: (a + b) / 2
trapezoid_perimeter = lambda a, b, c, d: a + b + c + d
trapezoid_diagonal_isosceles = lambda a, b, leg: math.sqrt(leg * leg + a * b)
kite_area_diagonals = lambda d1, d2: d1 * d2 / 2
kite_area_sides_angle = lambda a, b, theta: a * b * sin_deg(theta)     # theta between one long and one short side
kite_perimeter = lambda a, b: 2 * (a + b)

# --- Triangles ---
triangle_is_valid = lambda a, b, c: a + b > c and a + c > b and b + c > a
triangle_perimeter = lambda a, b, c: a + b + c
triangle_semiperimeter = lambda a, b, c: (a + b + c) / 2
triangle_area_bh = lambda base, height: base * height / 2
triangle_area_sas = lambda a, b, angle_c: 0.5 * a * b * sin_deg(angle_c)
triangle_area_asa = lambda angle_a, side_c, angle_b: side_c ** 2 * sin_deg(angle_a) * sin_deg(angle_b) / (2 * sin_deg(angle_a + angle_b))
triangle_area_aas = lambda angle_a, angle_b, side_a: side_a ** 2 * sin_deg(angle_b) * sin_deg(180 - angle_a - angle_b) / (2 * sin_deg(angle_a))
triangle_area_coordinates = lambda x1, y1, x2, y2, x3, y3: abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
triangle_area_circumradius = lambda a, b, c, circumradius: a * b * c / (4 * circumradius)
triangle_area_inradius = lambda a, b, c, inradius: inradius * (a + b + c) / 2
equilateral_area_s = lambda s: SQRT3 / 4 * s * s
equilateral_height_s = lambda s: SQRT3 / 2 * s
equilateral_inradius_s = lambda s: s * SQRT3 / 6
equilateral_circumradius_s = lambda s: s / SQRT3
isosceles_area = lambda base, leg: base / 4 * math.sqrt(4 * leg * leg - base * base)
isosceles_height = lambda base, leg: math.sqrt(leg * leg - base * base / 4)
pythagorean_hypotenuse = lambda a, b: math.hypot(a, b)
pythagorean_leg = lambda hypotenuse, leg: math.sqrt(hypotenuse ** 2 - leg ** 2)
right_triangle_area = lambda a, b: a * b / 2
right_triangle_inradius = lambda a, b, c: (a + b - c) / 2
right_triangle_circumradius = lambda hypotenuse: hypotenuse / 2
right_triangle_altitude = lambda a, b: a * b / math.hypot(a, b)         # altitude onto the hypotenuse
triangle_45_45_90_hypotenuse = lambda leg: leg * SQRT2
triangle_30_60_90_sides = lambda short_leg: (short_leg, short_leg * SQRT3, 2 * short_leg)
is_right_triangle = lambda a, b, c: is_close(sum(sorted((a * a, b * b, c * c))[:2]), max(a * a, b * b, c * c))
is_pythagorean_triple = lambda a, b, c: a * a + b * b == c * c
pythagorean_triple = lambda m, n: (m * m - n * n, 2 * m * n, m * m + n * n)       # Euclid's formula, m > n > 0
law_of_cosines_side = lambda a, b, angle_c: math.sqrt(a * a + b * b - 2 * a * b * cos_deg(angle_c))
law_of_cosines_angle = lambda a, b, c: acos_deg(clamp((a * a + b * b - c * c) / (2 * a * b), -1, 1))     # angle opposite c
law_of_sines_side = lambda side_a, angle_a, angle_b: side_a * sin_deg(angle_b) / sin_deg(angle_a)
law_of_sines_circumdiameter = lambda side_a, angle_a: side_a / sin_deg(angle_a)
stewart_cevian = lambda a, b, c, m, n: math.sqrt((b * b * m + c * c * n) / a - m * n)      # cevian to side a split into m + n = a


def law_of_sines_angle(side_a, angle_a, side_b):
    """Possible angles B (degrees) given a, A and b -- the ambiguous SSA case. Returns a tuple."""
    s = side_b * sin_deg(angle_a) / side_a
    if is_close(s, 1.0, rel_tol=1e-12):
        return (90.0,)
    if s > 1 or s < -1:
        return ()
    b1 = asin_deg(s)
    b2 = 180 - b1
    options = [b1]
    if not is_close(b1, b2) and angle_a + b2 < 180:
        options.append(b2)
    return tuple(options)


def triangle_area_heron(a, b, c):
    """Area from three sides (Heron's formula, in Kahan's numerically stable form)."""
    a, b, c = sorted((a, b, c), reverse=True)
    return 0.25 * math.sqrt((a + (b + c)) * (c - (a - b)) * (c + (a - b)) * (a + (b - c)))


def triangle_angles(a, b, c):
    """The angles (A, B, C) in degrees opposite sides a, b, c."""
    cos_a = (b * b + c * c - a * a) / (2 * b * c)
    cos_b = (a * a + c * c - b * b) / (2 * a * c)
    cos_c = (a * a + b * b - c * c) / (2 * a * b)
    return tuple(math.degrees(math.acos(clamp(v, -1.0, 1.0))) for v in (cos_a, cos_b, cos_c))


triangle_inradius = lambda a, b, c: triangle_area_heron(a, b, c) / triangle_semiperimeter(a, b, c)
triangle_circumradius = lambda a, b, c: a * b * c / (4 * triangle_area_heron(a, b, c))
triangle_exradii = lambda a, b, c: tuple(triangle_area_heron(a, b, c) / (triangle_semiperimeter(a, b, c) - side) for side in (a, b, c))
triangle_heights = lambda a, b, c: tuple(2 * triangle_area_heron(a, b, c) / side for side in (a, b, c))
triangle_medians = lambda a, b, c: (0.5 * math.sqrt(2 * b * b + 2 * c * c - a * a), 0.5 * math.sqrt(2 * a * a + 2 * c * c - b * b), 0.5 * math.sqrt(2 * a * a + 2 * b * b - c * c))
triangle_angle_bisectors = lambda a, b, c: (math.sqrt(b * c * ((b + c) ** 2 - a * a)) / (b + c), math.sqrt(a * c * ((a + c) ** 2 - b * b)) / (a + c), math.sqrt(a * b * ((a + b) ** 2 - c * c)) / (a + b))
triangle_nine_point_radius = lambda a, b, c: triangle_circumradius(a, b, c) / 2
triangle_euler_distance = lambda a, b, c: math.sqrt(triangle_circumradius(a, b, c) * (triangle_circumradius(a, b, c) - 2 * triangle_inradius(a, b, c)))   # distance between incentre and circumcentre


def triangle_type(a, b, c):
    """Classifies a triangle by sides and angles, e.g. 'scalene acute'."""
    if not triangle_is_valid(a, b, c):
        raise ValueError("these sides cannot form a triangle")
    if is_close(a, b) and is_close(b, c):
        sides = "equilateral"
    elif is_close(a, b) or is_close(b, c) or is_close(a, c):
        sides = "isosceles"
    else:
        sides = "scalene"
    x, y, z = sorted((a, b, c))
    if is_close(x * x + y * y, z * z):
        angle = "right"
    elif x * x + y * y < z * z:
        angle = "obtuse"
    else:
        angle = "acute"
    return f"{sides} {angle}"


triangle_centroid = lambda x1, y1, x2, y2, x3, y3: ((x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3)


def triangle_circumcenter(x1, y1, x2, y2, x3, y3):
    """Centre of the circle through three points."""
    d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if d == 0:
        raise ValueError("the points lie on one line")
    s1, s2, s3 = x1 * x1 + y1 * y1, x2 * x2 + y2 * y2, x3 * x3 + y3 * y3
    return ((s1 * (y2 - y3) + s2 * (y3 - y1) + s3 * (y1 - y2)) / d,
            (s1 * (x3 - x2) + s2 * (x1 - x3) + s3 * (x2 - x1)) / d)


def triangle_incenter(x1, y1, x2, y2, x3, y3):
    """Centre of the largest circle inside the triangle."""
    a = math.hypot(x2 - x3, y2 - y3)
    b = math.hypot(x1 - x3, y1 - y3)
    c = math.hypot(x1 - x2, y1 - y2)
    total = a + b + c
    return (a * x1 + b * x2 + c * x3) / total, (a * y1 + b * y2 + c * y3) / total


def triangle_orthocenter(x1, y1, x2, y2, x3, y3):
    """Point where the three altitudes meet (H = A + B + C - 2 * circumcentre)."""
    ox, oy = triangle_circumcenter(x1, y1, x2, y2, x3, y3)
    return x1 + x2 + x3 - 2 * ox, y1 + y2 + y3 - 2 * oy


points_are_collinear = lambda x1, y1, x2, y2, x3, y3: is_close(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2), 0, abs_tol=1e-12)

# --- Quadrilaterals ---
quadrilateral_area_diagonals = lambda d1, d2, theta: 0.5 * d1 * d2 * sin_deg(theta)
ptolemy_diagonal = lambda a, b, c, d, other_diagonal: (a * c + b * d) / other_diagonal      # cyclic quadrilateral: e * f = ac + bd


def cyclic_quadrilateral_area(a, b, c, d):
    """Brahmagupta's formula for a quadrilateral inscribed in a circle."""
    s = (a + b + c + d) / 2
    return math.sqrt((s - a) * (s - b) * (s - c) * (s - d))


def quadrilateral_area_bretschneider(a, b, c, d, angle_a, angle_c):
    """Bretschneider's formula: any quadrilateral from four sides and two opposite angles."""
    s = (a + b + c + d) / 2
    return math.sqrt((s - a) * (s - b) * (s - c) * (s - d) - a * b * c * d * cos_deg((angle_a + angle_c) / 2) ** 2)


def trapezoid_height_from_sides(a, b, c, d):
    """Height of a trapezoid with parallel sides a and b (a != b) and legs c and d."""
    long_base, short_base = max(a, b), min(a, b)
    return 2 * triangle_area_heron(long_base - short_base, c, d) / (long_base - short_base)


trapezoid_area_sides = lambda a, b, c, d: (a + b) / 2 * trapezoid_height_from_sides(a, b, c, d)

# --- Regular Polygons ---
regular_polygon_area = lambda n, s: n * s * s / (4 * math.tan(PI / n))
regular_polygon_perimeter = lambda n, s: n * s
regular_polygon_apothem = lambda n, s: s / (2 * math.tan(PI / n))
regular_polygon_circumradius = lambda n, s: s / (2 * math.sin(PI / n))
regular_polygon_side_from_circumradius = lambda n, circumradius: 2 * circumradius * math.sin(PI / n)
regular_polygon_area_circumradius = lambda n, circumradius: n * circumradius ** 2 * math.sin(TAU / n) / 2
regular_polygon_interior_angle = lambda n: (n - 2) * 180 / n
regular_polygon_exterior_angle = lambda n: 360 / n
regular_polygon_central_angle = lambda n: 360 / n
polygon_interior_angle_sum = lambda n: (n - 2) * 180
polygon_diagonal_count = lambda n: n * (n - 3) // 2
hexagon_area_s = lambda s: 3 * SQRT3 / 2 * s * s
pentagon_area_s = lambda s: 0.25 * math.sqrt(5 * (5 + 2 * SQRT5)) * s * s
octagon_area_s = lambda s: 2 * (1 + SQRT2) * s * s
pick_theorem_area = lambda interior_points, boundary_points: interior_points + boundary_points / 2 - 1
euler_characteristic = lambda vertices, edges, faces: vertices - edges + faces


def polygon_area_shoelace(points):
    """Area of any simple polygon from its corner points [(x, y), ...] (shoelace formula)."""
    n = len(points)
    return abs(sum(points[i][0] * points[(i + 1) % n][1] - points[(i + 1) % n][0] * points[i][1] for i in range(n))) / 2


def polygon_perimeter_points(points):
    """Perimeter of a polygon from its corner points."""
    n = len(points)
    return sum(math.hypot(points[(i + 1) % n][0] - points[i][0], points[(i + 1) % n][1] - points[i][1]) for i in range(n))


def polygon_centroid(points):
    """Centre of mass of a simple polygon given as [(x, y), ...]."""
    n = len(points)
    area2 = 0.0
    cx = cy = 0.0
    for i in range(n):
        x0, y0 = points[i]
        x1, y1 = points[(i + 1) % n]
        cross = x0 * y1 - x1 * y0
        area2 += cross
        cx += (x0 + x1) * cross
        cy += (y0 + y1) * cross
    return cx / (3 * area2), cy / (3 * area2)


def point_in_polygon(x, y, points):
    """True if (x, y) is inside the polygon (ray casting)."""
    inside = False
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            inside = not inside
    return inside


def convex_hull(points):
    """Smallest convex polygon around a set of points (Andrew's monotone chain)."""
    pts = sorted(set(map(tuple, points)))
    if len(pts) <= 2:
        return pts

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


# --- More Circle Formulas (extra to the ones above) ---
circle_segment_area_r = lambda r, theta: r ** 2 / 2 * (math.radians(theta) - math.sin(math.radians(theta)))
circle_segment_height_r = lambda r, theta: r * (1 - math.cos(math.radians(theta) / 2))
circle_chord_from_distance = lambda r, distance: 2 * math.sqrt(r ** 2 - distance ** 2)
circle_distance_to_chord = lambda r, chord: math.sqrt(r ** 2 - (chord / 2) ** 2)
circle_radius_from_chord_sagitta = lambda chord, sagitta: chord ** 2 / (8 * sagitta) + sagitta / 2
circle_tangent_length = lambda distance_from_center, r: math.sqrt(distance_from_center ** 2 - r ** 2)
circle_power_of_point = lambda distance_from_center, r: distance_from_center ** 2 - r ** 2
circle_inscribed_angle = lambda arc_angle: arc_angle / 2
circle_angle_two_chords = lambda arc1, arc2: (arc1 + arc2) / 2
circle_angle_two_secants = lambda far_arc, near_arc: (far_arc - near_arc) / 2
circle_sector_perimeter_r_pi = lambda r, theta: 2 * r + circle_arc_length_r_pi(r, theta)
circle_common_tangents = lambda distance, r1, r2: (math.sqrt(distance ** 2 - (r1 - r2) ** 2), math.sqrt(distance ** 2 - (r1 + r2) ** 2))    # (outer, inner)
descartes_circle_theorem = lambda k1, k2, k3: (k1 + k2 + k3 + 2 * math.sqrt(k1 * k2 + k2 * k3 + k3 * k1), k1 + k2 + k3 - 2 * math.sqrt(k1 * k2 + k2 * k3 + k3 * k1))
circle_from_general_equation = lambda d, e, f: (-d / 2, -e / 2, math.sqrt(d * d / 4 + e * e / 4 - f))       # x^2 + y^2 + dx + ey + f = 0 -> (h, k, r)
annulus_area_pi = lambda outer, inner: PI * (outer ** 2 - inner ** 2)
annulus_area = lambda outer, inner: _with_pi(outer ** 2 - inner ** 2)


def circle_from_three_points(x1, y1, x2, y2, x3, y3):
    """Circle through three points -> (centre_x, centre_y, radius)."""
    cx, cy = triangle_circumcenter(x1, y1, x2, y2, x3, y3)
    return cx, cy, math.hypot(x1 - cx, y1 - cy)


def circle_lens_area(r1, r2, distance):
    """Overlap area of two circles with radii r1, r2 whose centres are `distance` apart."""
    if distance >= r1 + r2:
        return 0.0
    if distance <= abs(r1 - r2):
        return PI * min(r1, r2) ** 2
    a1 = math.acos((distance ** 2 + r1 ** 2 - r2 ** 2) / (2 * distance * r1))
    a2 = math.acos((distance ** 2 + r2 ** 2 - r1 ** 2) / (2 * distance * r2))
    return r1 ** 2 * (a1 - math.sin(2 * a1) / 2) + r2 ** 2 * (a2 - math.sin(2 * a2) / 2)


# --- Ellipse ---
ellipse_area_pi = lambda a, b: PI * a * b
ellipse_area = lambda a, b: _with_pi(a * b)
ellipse_eccentricity = lambda a, b: math.sqrt(1 - (min(a, b) / max(a, b)) ** 2)
ellipse_focal_distance = lambda a, b: math.sqrt(abs(a * a - b * b))
ellipse_latus_rectum = lambda a, b: 2 * min(a, b) ** 2 / max(a, b)
ellipse_perimeter_ramanujan = lambda a, b: PI * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))
ellipse_perimeter_ramanujan2 = lambda a, b: PI * (a + b) * (1 + 3 * ((a - b) / (a + b)) ** 2 / (10 + math.sqrt(4 - 3 * ((a - b) / (a + b)) ** 2)))
ellipse_perimeter_integral = lambda a, b: 4 * integral_gauss(lambda t: math.sqrt(a * a * math.sin(t) ** 2 + b * b * math.cos(t) ** 2), 0, PI / 2, 40)

# --- Cube & Cuboid ---
cube_volume_s = lambda s: s ** 3
cube_surface_area_s = lambda s: 6 * s * s
cube_space_diagonal_s = lambda s: s * SQRT3
cube_face_diagonal_s = lambda s: s * SQRT2
cube_inradius_s = lambda s: s / 2
cube_midradius_s = lambda s: s * SQRT2 / 2
cube_circumradius_s = lambda s: s * SQRT3 / 2
cube_side_from_volume = lambda v: v ** (1 / 3)
cuboid_volume = lambda length, width, height: length * width * height
cuboid_surface_area = lambda length, width, height: 2 * (length * width + length * height + width * height)
cuboid_space_diagonal = lambda length, width, height: math.sqrt(length ** 2 + width ** 2 + height ** 2)
cuboid_face_diagonals = lambda length, width, height: (math.hypot(length, width), math.hypot(length, height), math.hypot(width, height))

# --- Sphere ---
sphere_volume_r_pi = lambda r: 4 / 3 * PI * r ** 3
sphere_volume_r = lambda r: _with_pi(4 / 3 * r ** 3)
sphere_volume_d_pi = lambda d: 4 / 3 * PI * (d / 2) ** 3
sphere_volume_d = lambda d: _with_pi(4 / 3 * (d / 2) ** 3)
sphere_surface_area_r_pi = lambda r: 4 * PI * r ** 2
sphere_surface_area_r = lambda r: _with_pi(4 * r ** 2)
sphere_surface_area_d_pi = lambda d: PI * d ** 2
sphere_surface_area_d = lambda d: _with_pi(d ** 2)
sphere_radius_v_pi = lambda v: (3 * v / (4 * PI)) ** (1 / 3)
sphere_radius_sa_pi = lambda sa: math.sqrt(sa / (4 * PI))
hemisphere_volume_r_pi = lambda r: 2 / 3 * PI * r ** 3
hemisphere_volume_r = lambda r: _with_pi(2 / 3 * r ** 3)
hemisphere_curved_area_r_pi = lambda r: 2 * PI * r ** 2
hemisphere_curved_area_r = lambda r: _with_pi(2 * r ** 2)
hemisphere_total_area_r_pi = lambda r: 3 * PI * r ** 2
hemisphere_total_area_r = lambda r: _with_pi(3 * r ** 2)
spherical_cap_volume_pi = lambda r, h: PI * h * h * (3 * r - h) / 3
spherical_cap_volume = lambda r, h: _with_pi(h * h * (3 * r - h) / 3)
spherical_cap_volume_base_pi = lambda a, h: PI * h * (3 * a * a + h * h) / 6          # a = radius of the cap's flat base
spherical_cap_curved_area_pi = lambda r, h: 2 * PI * r * h
spherical_cap_curved_area = lambda r, h: _with_pi(2 * r * h)
spherical_cap_total_area_pi = lambda r, h: PI * h * (4 * r - h)
spherical_cap_base_radius = lambda r, h: math.sqrt(h * (2 * r - h))
spherical_zone_area_pi = lambda r, h: 2 * PI * r * h
spherical_zone_area = lambda r, h: _with_pi(2 * r * h)
spherical_segment_volume_pi = lambda r1, r2, h: PI * h * (3 * r1 * r1 + 3 * r2 * r2 + h * h) / 6
spherical_sector_volume_pi = lambda r, h: 2 / 3 * PI * r * r * h
spherical_sector_volume = lambda r, h: _with_pi(2 / 3 * r * r * h)
spherical_lune_area_pi = lambda r, theta: theta / 360 * 4 * PI * r * r
spherical_lune_area = lambda r, theta: _with_pi(theta / 360 * 4 * r * r)
spherical_triangle_area = lambda r, angle_a, angle_b, angle_c: r * r * math.radians(angle_a + angle_b + angle_c - 180)
solid_angle_cone = lambda half_angle: TAU * (1 - cos_deg(half_angle))                  # steradians

# --- Cylinder, Cone & Friends ---
cylinder_volume_r_pi = lambda r, h: PI * r * r * h
cylinder_volume_r = lambda r, h: _with_pi(r * r * h)
cylinder_lateral_area_r_pi = lambda r, h: 2 * PI * r * h
cylinder_lateral_area_r = lambda r, h: _with_pi(2 * r * h)
cylinder_total_area_r_pi = lambda r, h: 2 * PI * r * (r + h)
cylinder_total_area_r = lambda r, h: _with_pi(2 * r * (r + h))
cylinder_hollow_volume_pi = lambda outer, inner, h: PI * h * (outer ** 2 - inner ** 2)
cylinder_hollow_volume = lambda outer, inner, h: _with_pi(h * (outer ** 2 - inner ** 2))
cylinder_height_from_volume_pi = lambda v, r: v / (PI * r * r)
cylinder_radius_from_volume_pi = lambda v, h: math.sqrt(v / (PI * h))
cylinder_diagonal = lambda r, h: math.sqrt(4 * r * r + h * h)
cone_slant_height = lambda r, h: math.hypot(r, h)
cone_height_from_slant = lambda r, slant: math.sqrt(slant ** 2 - r ** 2)
cone_volume_r_pi = lambda r, h: PI * r * r * h / 3
cone_volume_r = lambda r, h: _with_pi(r * r * h / 3)
cone_lateral_area_r_pi = lambda r, h: PI * r * math.hypot(r, h)
cone_lateral_area_r = lambda r, h: _with_pi(r * math.hypot(r, h))
cone_total_area_r_pi = lambda r, h: PI * r * (r + math.hypot(r, h))
cone_total_area_r = lambda r, h: _with_pi(r * (r + math.hypot(r, h)))
cone_apex_angle = lambda r, h: 2 * atan_deg(r / h)
cone_unrolled_sector_angle = lambda r, slant: 360 * r / slant
frustum_slant_height = lambda r1, r2, h: math.sqrt(h * h + (r1 - r2) ** 2)
frustum_volume_pi = lambda r1, r2, h: PI * h * (r1 * r1 + r1 * r2 + r2 * r2) / 3
frustum_volume = lambda r1, r2, h: _with_pi(h * (r1 * r1 + r1 * r2 + r2 * r2) / 3)
frustum_lateral_area_pi = lambda r1, r2, h: PI * (r1 + r2) * math.sqrt(h * h + (r1 - r2) ** 2)
frustum_lateral_area = lambda r1, r2, h: _with_pi((r1 + r2) * math.sqrt(h * h + (r1 - r2) ** 2))
frustum_total_area_pi = lambda r1, r2, h: PI * ((r1 + r2) * math.sqrt(h * h + (r1 - r2) ** 2) + r1 * r1 + r2 * r2)
capsule_volume_pi = lambda r, cylinder_height: PI * r * r * cylinder_height + 4 / 3 * PI * r ** 3
capsule_surface_area_pi = lambda r, cylinder_height: 2 * PI * r * cylinder_height + 4 * PI * r * r
paraboloid_volume_pi = lambda r, h: PI * r * r * h / 2
paraboloid_surface_area_pi = lambda r, h: PI * r / (6 * h * h) * ((r * r + 4 * h * h) ** 1.5 - r ** 3)
torus_volume_pi = lambda major, minor: 2 * PI ** 2 * major * minor ** 2
torus_volume = lambda major, minor: f"{2 * major * minor ** 2}π²"
torus_surface_area_pi = lambda major, minor: 4 * PI ** 2 * major * minor
torus_surface_area = lambda major, minor: f"{4 * major * minor}π²"
ellipsoid_volume_pi = lambda a, b, c: 4 / 3 * PI * a * b * c
ellipsoid_volume = lambda a, b, c: _with_pi(4 / 3 * a * b * c)
ellipsoid_surface_area_approx = lambda a, b, c, p=1.6075: 4 * PI * (((a * b) ** p + (a * c) ** p + (b * c) ** p) / 3) ** (1 / p)     # Knud Thomsen


def spheroid_surface_area_pi(equatorial, polar):
    """Exact surface area of an oblate or prolate spheroid (equatorial radius a, polar radius c)."""
    a, c = equatorial, polar
    if is_close(a, c):
        return 4 * PI * a * a
    if c > a:
        e = math.sqrt(1 - a * a / (c * c))
        return 2 * PI * a * a * (1 + c / (a * e) * math.asin(e))
    e = math.sqrt(1 - c * c / (a * a))
    return 2 * PI * a * a * (1 + (1 - e * e) / e * math.atanh(e))


# --- Pyramids & Prisms ---
pyramid_volume = lambda base_area, height: base_area * height / 3
pyramid_square_slant_height = lambda base, height: math.sqrt(height ** 2 + (base / 2) ** 2)
pyramid_square_lateral_area = lambda base, height: 2 * base * math.sqrt(height ** 2 + (base / 2) ** 2)
pyramid_square_total_area = lambda base, height: base * base + 2 * base * math.sqrt(height ** 2 + (base / 2) ** 2)
pyramid_square_edge = lambda base, height: math.sqrt(height ** 2 + base ** 2 / 2)
pyramid_regular_volume = lambda n, side, height: regular_polygon_area(n, side) * height / 3
pyramid_regular_lateral_area = lambda n, side, slant: n * side * slant / 2
pyramid_frustum_volume = lambda area1, area2, height: height / 3 * (area1 + area2 + math.sqrt(area1 * area2))
prism_volume = lambda base_area, height: base_area * height
prism_lateral_area = lambda base_perimeter, height: base_perimeter * height
prism_total_area = lambda base_area, base_perimeter, height: 2 * base_area + base_perimeter * height
prism_triangular_volume = lambda base, triangle_height, length: base * triangle_height / 2 * length
prism_regular_volume = lambda n, side, height: regular_polygon_area(n, side) * height

# --- Platonic Solids (edge length a) ---
tetrahedron_volume_a = lambda a: a ** 3 / (6 * SQRT2)
tetrahedron_surface_area_a = lambda a: SQRT3 * a * a
tetrahedron_height_a = lambda a: a * math.sqrt(2 / 3)
tetrahedron_circumradius_a = lambda a: a * math.sqrt(6) / 4
tetrahedron_inradius_a = lambda a: a * math.sqrt(6) / 12
octahedron_volume_a = lambda a: SQRT2 / 3 * a ** 3
octahedron_surface_area_a = lambda a: 2 * SQRT3 * a * a
octahedron_circumradius_a = lambda a: a / SQRT2
octahedron_inradius_a = lambda a: a * math.sqrt(6) / 6
dodecahedron_volume_a = lambda a: (15 + 7 * SQRT5) / 4 * a ** 3
dodecahedron_surface_area_a = lambda a: 3 * math.sqrt(25 + 10 * SQRT5) * a * a
dodecahedron_circumradius_a = lambda a: a * SQRT3 * (1 + SQRT5) / 4
dodecahedron_inradius_a = lambda a: a / 2 * math.sqrt((25 + 11 * SQRT5) / 10)
icosahedron_volume_a = lambda a: 5 * (3 + SQRT5) / 12 * a ** 3
icosahedron_surface_area_a = lambda a: 5 * SQRT3 * a * a
icosahedron_circumradius_a = lambda a: a / 4 * math.sqrt(10 + 2 * SQRT5)
icosahedron_inradius_a = lambda a: SQRT3 * (3 + SQRT5) / 12 * a

# --- Centroids ---
centroid_semicircle_r = lambda r: 4 * r / (3 * PI)          # distance from the flat edge
centroid_hemisphere_r = lambda r: 3 * r / 8                 # distance from the flat face
centroid_cone_h = lambda h: h / 4                           # distance from the base
centroid_pyramid_h = lambda h: h / 4
centroid_triangle_h = lambda h: h / 3
centroid_circular_sector_r = lambda r, theta: 2 * r * sin_deg(theta / 2) / (3 * math.radians(theta / 2))     # distance from the centre, theta = full sector angle

# --- Coordinate Geometry (2D) ---
distance_2d = lambda x1, y1, x2, y2: math.hypot(x2 - x1, y2 - y1)
distance_3d = lambda x1, y1, z1, x2, y2, z2: math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
midpoint_2d = lambda x1, y1, x2, y2: ((x1 + x2) / 2, (y1 + y2) / 2)
midpoint_3d = lambda x1, y1, z1, x2, y2, z2: ((x1 + x2) / 2, (y1 + y2) / 2, (z1 + z2) / 2)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
perpendicular_slope = lambda m: -1 / m
section_formula_internal = lambda x1, y1, x2, y2, m, n: ((m * x2 + n * x1) / (m + n), (m * y2 + n * y1) / (m + n))
section_formula_external = lambda x1, y1, x2, y2, m, n: ((m * x2 - n * x1) / (m - n), (m * y2 - n * y1) / (m - n))
line_from_two_points = lambda x1, y1, x2, y2: (y2 - y1, x1 - x2, x2 * y1 - x1 * y2)        # (A, B, C) for Ax + By + C = 0
line_from_slope_point = lambda m, x1, y1: (m, -1, y1 - m * x1)
distance_point_to_line = lambda x0, y0, a, b, c: abs(a * x0 + b * y0 + c) / math.hypot(a, b)
distance_between_parallel_lines = lambda a, b, c1, c2: abs(c1 - c2) / math.hypot(a, b)
angle_between_lines_slopes = lambda m1, m2: 90.0 if is_close(1 + m1 * m2, 0, abs_tol=1e-12) else atan_deg(abs((m1 - m2) / (1 + m1 * m2)))
line_intersection = lambda a1, b1, c1, a2, b2, c2: solve_2x2(a1, b1, -c1, a2, b2, -c2)
reflect_point_over_line = lambda x, y, a, b, c: (x - 2 * a * (a * x + b * y + c) / (a * a + b * b), y - 2 * b * (a * x + b * y + c) / (a * a + b * b))
perpendicular_bisector = lambda x1, y1, x2, y2: (x2 - x1, y2 - y1, -((x2 - x1) * (x1 + x2) / 2 + (y2 - y1) * (y1 + y2) / 2))
rotate_point = lambda x, y, angle, cx=0, cy=0: (cx + (x - cx) * cos_deg(angle) - (y - cy) * sin_deg(angle), cy + (x - cx) * sin_deg(angle) + (y - cy) * cos_deg(angle))
scale_point = lambda x, y, factor, cx=0, cy=0: (cx + (x - cx) * factor, cy + (y - cy) * factor)


def slope_intercept_from_points(x1, y1, x2, y2):
    """Returns (m, b) for y = mx + b through two points."""
    if x1 == x2:
        raise ValueError("vertical line has no slope-intercept form")
    m = (y2 - y1) / (x2 - x1)
    return m, y1 - m * x1


# --- Conic Sections ---
parabola_focus = lambda a, h, k: (h, k + 1 / (4 * a))                  # y = a(x - h)^2 + k
parabola_directrix = lambda a, h, k: k - 1 / (4 * a)
parabola_latus_rectum = lambda a: 1 / abs(a)
hyperbola_eccentricity = lambda a, b: math.sqrt(1 + b * b / (a * a))
hyperbola_focal_distance = lambda a, b: math.sqrt(a * a + b * b)
hyperbola_asymptote_slope = lambda a, b: b / a


def conic_type(a, b, c):
    """Classifies Ax^2 + Bxy + Cy^2 + ... = 0 using the discriminant B^2 - 4AC."""
    d = b * b - 4 * a * c
    if d < 0:
        return "circle" if (is_close(a, c) and b == 0) else "ellipse"
    if d == 0:
        return "parabola"
    return "hyperbola"


# --- Vectors (lists or tuples of numbers) ---
vector_add = lambda a, b: [x + y for x, y in zip(a, b)]
vector_subtract = lambda a, b: [x - y for x, y in zip(a, b)]
vector_scale = lambda v, k: [k * x for x in v]
vector_magnitude = lambda v: math.sqrt(sum(x * x for x in v))
vector_normalize = lambda v: [x / math.sqrt(sum(y * y for y in v)) for x in v]
dot_product = lambda a, b: sum(x * y for x, y in zip(a, b))
cross_product_3d = lambda a, b: [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
cross_product_2d = lambda a, b: a[0] * b[1] - a[1] * b[0]
angle_between_vectors = lambda a, b: math.degrees(math.acos(clamp(dot_product(a, b) / (vector_magnitude(a) * vector_magnitude(b)), -1.0, 1.0)))
scalar_projection = lambda a, b: dot_product(a, b) / vector_magnitude(b)
vector_projection = lambda a, b: [dot_product(a, b) / dot_product(b, b) * x for x in b]
vector_rejection = lambda a, b: [x - p for x, p in zip(a, vector_projection(a, b))]
triple_scalar_product = lambda a, b, c: dot_product(a, cross_product_3d(b, c))
triple_vector_product = lambda a, b, c: cross_product_3d(a, cross_product_3d(b, c))
parallelogram_area_vectors = lambda a, b: vector_magnitude(cross_product_3d(a, b))
triangle_area_vectors = lambda a, b: vector_magnitude(cross_product_3d(a, b)) / 2
parallelepiped_volume = lambda a, b, c: abs(dot_product(a, cross_product_3d(b, c)))
tetrahedron_volume_vectors = lambda a, b, c: abs(dot_product(a, cross_product_3d(b, c))) / 6
vectors_are_parallel = lambda a, b: all(is_close(x, 0, abs_tol=1e-12) for x in cross_product_3d(a, b))
vectors_are_orthogonal = lambda a, b: is_close(dot_product(a, b), 0, abs_tol=1e-12)
direction_cosines = lambda v: [x / vector_magnitude(v) for x in v]
vector_lerp = lambda a, b, t: [x + (y - x) * t for x, y in zip(a, b)]
reflect_vector = lambda v, normal: [x - 2 * dot_product(v, normal) / dot_product(normal, normal) * n for x, n in zip(v, normal)]
euclidean_distance = lambda a, b: math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
manhattan_distance = lambda a, b: sum(abs(x - y) for x, y in zip(a, b))
chebyshev_distance = lambda a, b: max(abs(x - y) for x, y in zip(a, b))
minkowski_distance = lambda a, b, p: sum(abs(x - y) ** p for x, y in zip(a, b)) ** (1 / p)
hamming_distance = lambda a, b: sum(1 for x, y in zip(a, b) if x != y)
cosine_similarity = lambda a, b: dot_product(a, b) / (vector_magnitude(a) * vector_magnitude(b))


def gram_schmidt(vectors):
    """Turns a list of independent vectors into an orthonormal set."""
    basis = []
    for v in vectors:
        w = list(v)
        for u in basis:
            w = vector_subtract(w, vector_scale(u, dot_product(w, u)))
        length = vector_magnitude(w)
        if length > 1e-12:
            basis.append([x / length for x in w])
    return basis


# --- Planes & Lines in 3D ---
distance_point_plane = lambda point, a, b, c, d: abs(a * point[0] + b * point[1] + c * point[2] + d) / math.sqrt(a * a + b * b + c * c)
angle_between_planes = lambda n1, n2: math.degrees(math.acos(clamp(abs(dot_product(n1, n2)) / (vector_magnitude(n1) * vector_magnitude(n2)), 0.0, 1.0)))
distance_point_line_3d = lambda point, line_point, direction: vector_magnitude(cross_product_3d(vector_subtract(point, line_point), direction)) / vector_magnitude(direction)
distance_between_skew_lines = lambda p1, d1, p2, d2: abs(dot_product(vector_subtract(p2, p1), cross_product_3d(d1, d2))) / vector_magnitude(cross_product_3d(d1, d2))
angle_line_plane = lambda direction, normal: asin_deg(clamp(abs(dot_product(direction, normal)) / (vector_magnitude(direction) * vector_magnitude(normal)), 0.0, 1.0))
sphere_equation_radius = lambda d, e, f, g: math.sqrt((d / 2) ** 2 + (e / 2) ** 2 + (f / 2) ** 2 - g)       # x^2 + y^2 + z^2 + dx + ey + fz + g = 0


def plane_from_points(p1, p2, p3):
    """Plane through three points -> (A, B, C, D) for Ax + By + Cz + D = 0."""
    n = cross_product_3d(vector_subtract(p2, p1), vector_subtract(p3, p1))
    return n[0], n[1], n[2], -dot_product(n, p1)


def line_plane_intersection(line_point, direction, a, b, c, d):
    """Point where a line meets the plane Ax + By + Cz + D = 0."""
    denominator = a * direction[0] + b * direction[1] + c * direction[2]
    if denominator == 0:
        raise ValueError("the line is parallel to the plane")
    t = -(a * line_point[0] + b * line_point[1] + c * line_point[2] + d) / denominator
    return [line_point[i] + t * direction[i] for i in range(3)]

# --- Matrices (lists of rows, e.g. [[1, 2], [3, 4]]) ---
matrix_transpose = lambda m: [list(row) for row in zip(*m)]
matrix_add = lambda a, b: [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]
matrix_subtract = lambda a, b: [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]
matrix_scale = lambda m, k: [[k * x for x in row] for row in m]
matrix_multiply = lambda a, b: [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]
matrix_trace = lambda m: sum(m[i][i] for i in range(len(m)))
matrix_frobenius_norm = lambda m: math.sqrt(sum(x * x for row in m for x in row))
matrix_is_symmetric = lambda m: all(is_close(m[i][j], m[j][i]) for i in range(len(m)) for j in range(len(m)))
determinant_2x2 = lambda a, b, c, d: a * d - b * c
rotation_matrix_2d = lambda angle: [[cos_deg(angle), -sin_deg(angle)], [sin_deg(angle), cos_deg(angle)]]
rotation_matrix_x = lambda angle: [[1, 0, 0], [0, cos_deg(angle), -sin_deg(angle)], [0, sin_deg(angle), cos_deg(angle)]]
rotation_matrix_y = lambda angle: [[cos_deg(angle), 0, sin_deg(angle)], [0, 1, 0], [-sin_deg(angle), 0, cos_deg(angle)]]
rotation_matrix_z = lambda angle: [[cos_deg(angle), -sin_deg(angle), 0], [sin_deg(angle), cos_deg(angle), 0], [0, 0, 1]]


def matrix_identity(n):
    """The n x n identity matrix."""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def matrix_determinant(m):
    """Determinant of a square matrix (Bareiss algorithm, exact for integer matrices)."""
    n = len(m)
    a = [list(row) for row in m]
    exact = all(isinstance(x, int) for row in a for x in row)
    sign_ = 1
    previous = 1
    for k in range(n - 1):
        pivot = max(range(k, n), key=lambda i: abs(a[i][k]))
        if a[pivot][k] == 0:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign_ = -sign_
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                value = a[i][j] * a[k][k] - a[i][k] * a[k][j]
                a[i][j] = value // previous if exact else value / previous
        previous = a[k][k]
    return sign_ * a[n - 1][n - 1] + 0


def determinant_3x3(m):
    """Determinant of a 3x3 matrix (rule of Sarrus)."""
    return (m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1]
            - m[0][2] * m[1][1] * m[2][0] - m[0][0] * m[1][2] * m[2][1] - m[0][1] * m[1][0] * m[2][2])


def matrix_minor(m, row, col):
    """The matrix left after deleting one row and one column."""
    return [[x for j, x in enumerate(r) if j != col] for i, r in enumerate(m) if i != row]


def matrix_cofactors(m):
    """Matrix of cofactors."""
    n = len(m)
    if n == 1:
        return [[1]]
    return [[(-1) ** (i + j) * matrix_determinant(matrix_minor(m, i, j)) for j in range(n)] for i in range(n)]


matrix_adjugate = lambda m: matrix_transpose(matrix_cofactors(m))


def matrix_inverse(m):
    """Inverse of a square matrix (Gauss-Jordan elimination)."""
    n = len(m)
    a = [[float(x) for x in row] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(m)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda i: abs(a[i][col]))
        if abs(a[pivot][col]) < 1e-12:
            raise ValueError("matrix is singular (it has no inverse)")
        a[col], a[pivot] = a[pivot], a[col]
        scale = a[col][col]
        a[col] = [x / scale for x in a[col]]
        for i in range(n):
            if i != col:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[col])]
    return [row[n:] for row in a]


def matrix_solve(a, b):
    """Solves A x = b for x (Gaussian elimination with partial pivoting)."""
    n = len(a)
    m = [[float(x) for x in row] + [float(b[i])] for i, row in enumerate(a)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda i: abs(m[i][col]))
        if abs(m[pivot][col]) < 1e-12:
            raise ValueError("no unique solution")
        m[col], m[pivot] = m[pivot], m[col]
        for i in range(col + 1, n):
            factor = m[i][col] / m[col][col]
            m[i] = [x - factor * y for x, y in zip(m[i], m[col])]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))) / m[i][i]
    return x


def cramers_rule(a, b):
    """Solves A x = b using determinants (Cramer's rule)."""
    det = matrix_determinant(a)
    if det == 0:
        raise ValueError("no unique solution (determinant is 0)")
    result = []
    for col in range(len(a)):
        replaced = [row[:col] + [b[i]] + row[col + 1:] for i, row in enumerate(a)]
        result.append(matrix_determinant(replaced) / det)
    return result


def matrix_rank(m, tolerance=1e-10):
    """Rank of a matrix (row reduction)."""
    a = [[float(x) for x in row] for row in m]
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = max(range(rank, rows), key=lambda i: abs(a[i][col]), default=None)
        if pivot is None or abs(a[pivot][col]) < tolerance:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for i in range(rank + 1, rows):
            factor = a[i][col] / a[rank][col]
            a[i] = [x - factor * y for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def matrix_power(m, k):
    """Matrix raised to an integer power (negative powers use the inverse)."""
    if k < 0:
        m = matrix_inverse(m)
        k = -k
    result = matrix_identity(len(m))
    base = m
    while k:
        if k & 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        k >>= 1
    return result


def eigenvalues_2x2(m):
    """Eigenvalues of a 2x2 matrix (roots of lambda^2 - trace*lambda + determinant)."""
    return quadratic_roots(1, -(m[0][0] + m[1][1]), m[0][0] * m[1][1] - m[0][1] * m[1][0])


def eigenvalues_3x3(m):
    """Eigenvalues of a 3x3 matrix (roots of its characteristic cubic)."""
    trace = matrix_trace(m)
    minors = (m[0][0] * m[1][1] - m[0][1] * m[1][0]) + (m[0][0] * m[2][2] - m[0][2] * m[2][0]) + (m[1][1] * m[2][2] - m[1][2] * m[2][1])
    return cubic_roots(1, -trace, minors, -determinant_3x3(m))


def power_iteration(m, iterations=1000, tolerance=1e-12):
    """Dominant eigenvalue and eigenvector of a square matrix -> (value, vector)."""
    n = len(m)
    v = [1.0] * n
    value = 0.0
    for _ in range(iterations):
        w = [sum(m[i][j] * v[j] for j in range(n)) for i in range(n)]
        norm = vector_magnitude(w)
        if norm == 0:
            return 0.0, v
        w = [x / norm for x in w]
        new_value = sum(w[i] * sum(m[i][j] * w[j] for j in range(n)) for i in range(n))
        if abs(new_value - value) < tolerance:
            return new_value, w
        value, v = new_value, w
    return value, v


# --- Complex Numbers (built-in complex type, e.g. 3 + 4j) ---
complex_modulus = lambda z: math.hypot(z.real, z.imag)
complex_argument = lambda z: math.degrees(math.atan2(z.imag, z.real))
complex_conjugate = lambda z: complex(z.real, -z.imag)
complex_polar = lambda z: (math.hypot(z.real, z.imag), math.degrees(math.atan2(z.imag, z.real)))
complex_from_polar = lambda r, theta: complex(r * cos_deg(theta), r * sin_deg(theta))
complex_exp = lambda z: math.exp(z.real) * complex(math.cos(z.imag), math.sin(z.imag))
complex_ln = lambda z: complex(math.log(math.hypot(z.real, z.imag)), math.atan2(z.imag, z.real))
complex_sin = lambda z: complex(math.sin(z.real) * math.cosh(z.imag), math.cos(z.real) * math.sinh(z.imag))
complex_cos = lambda z: complex(math.cos(z.real) * math.cosh(z.imag), -math.sin(z.real) * math.sinh(z.imag))
complex_sinh = lambda z: complex(math.sinh(z.real) * math.cos(z.imag), math.cosh(z.real) * math.sin(z.imag))
complex_cosh = lambda z: complex(math.cosh(z.real) * math.cos(z.imag), math.sinh(z.real) * math.sin(z.imag))
complex_power = lambda z, n: math.hypot(z.real, z.imag) ** n * complex(math.cos(n * math.atan2(z.imag, z.real)), math.sin(n * math.atan2(z.imag, z.real)))      # De Moivre
complex_sqrt = lambda z: complex_power(z, 0.5)
euler_formula = lambda angle: complex(cos_deg(angle), sin_deg(angle))                  # e^(i*angle)
complex_distance = lambda z1, z2: math.hypot(z1.real - z2.real, z1.imag - z2.imag)


def complex_nth_roots(z, n):
    """All n complex n-th roots of z."""
    r = math.hypot(z.real, z.imag) ** (1 / n)
    theta = math.atan2(z.imag, z.real)
    return [r * complex(math.cos((theta + TAU * k) / n), math.sin((theta + TAU * k) / n)) for k in range(n)]


roots_of_unity = lambda n: complex_nth_roots(complex(1, 0), n)

# --- Statistics (data is a list of numbers) ---
def mean(data):
    """Arithmetic mean."""
    return sum(data) / len(data)


average = mean


def median(data):
    """Middle value (average of the two middle values for an even count)."""
    s = sorted(data)
    mid = len(s) // 2
    return s[mid] if len(s) % 2 else (s[mid - 1] + s[mid]) / 2


def mode(data):
    """List of the most frequent value(s)."""
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1
    top = max(counts.values())
    return sorted(k for k, v in counts.items() if v == top)


range_of = lambda data: max(data) - min(data)
midrange = lambda data: (max(data) + min(data)) / 2
variance_population = lambda data: sum((x - mean(data)) ** 2 for x in data) / len(data)
variance_sample = lambda data: sum((x - mean(data)) ** 2 for x in data) / (len(data) - 1)
std_dev_population = lambda data: math.sqrt(variance_population(data))
std_dev_sample = lambda data: math.sqrt(variance_sample(data))
standard_error = lambda data: std_dev_sample(data) / math.sqrt(len(data))
coefficient_of_variation = lambda data: std_dev_sample(data) / mean(data)
mean_absolute_deviation = lambda data: sum(abs(x - mean(data)) for x in data) / len(data)
median_absolute_deviation = lambda data: median([abs(x - median(data)) for x in data])
geometric_mean = lambda data: math.exp(sum(math.log(x) for x in data) / len(data))
harmonic_mean = lambda data: len(data) / sum(1 / x for x in data)
quadratic_mean = lambda data: math.sqrt(sum(x * x for x in data) / len(data))
weighted_mean = lambda values, weights: sum(v * w for v, w in zip(values, weights)) / sum(weights)
z_scores = lambda data: [(x - mean(data)) / std_dev_population(data) for x in data]
cumulative_sum = lambda data: [sum(data[:i + 1]) for i in range(len(data))]
moving_average = lambda data, window: [sum(data[i:i + window]) / window for i in range(len(data) - window + 1)]
min_max_normalize = lambda data: [(x - min(data)) / (max(data) - min(data)) for x in data]
skewness = lambda data: (sum((x - mean(data)) ** 3 for x in data) / len(data)) / variance_population(data) ** 1.5
kurtosis_excess = lambda data: (sum((x - mean(data)) ** 4 for x in data) / len(data)) / variance_population(data) ** 2 - 3
covariance_population = lambda xs, ys: sum((x - mean(xs)) * (y - mean(ys)) for x, y in zip(xs, ys)) / len(xs)
covariance_sample = lambda xs, ys: sum((x - mean(xs)) * (y - mean(ys)) for x, y in zip(xs, ys)) / (len(xs) - 1)
pearson_correlation = lambda xs, ys: covariance_population(xs, ys) / (std_dev_population(xs) * std_dev_population(ys))
mse = lambda actual, predicted: sum((a - p) ** 2 for a, p in zip(actual, predicted)) / len(actual)
rmse = lambda actual, predicted: math.sqrt(mse(actual, predicted))
mae = lambda actual, predicted: sum(abs(a - p) for a, p in zip(actual, predicted)) / len(actual)
r_squared = lambda actual, predicted: 1 - sum((a - p) ** 2 for a, p in zip(actual, predicted)) / sum((a - mean(actual)) ** 2 for a in actual)
entropy = lambda probabilities, base=2: -sum(p * math.log(p, base) for p in probabilities if p > 0)
kl_divergence = lambda p, q, base=2: sum(a * math.log(a / b, base) for a, b in zip(p, q) if a > 0)
cross_entropy = lambda p, q, base=2: -sum(a * math.log(b, base) for a, b in zip(p, q) if a > 0)
expected_value = lambda values, probabilities: sum(v * p for v, p in zip(values, probabilities))
variance_discrete = lambda values, probabilities: sum(p * (v - expected_value(values, probabilities)) ** 2 for v, p in zip(values, probabilities))


def trimmed_mean(data, proportion=0.1):
    """Mean after cutting `proportion` of the values off each end."""
    s = sorted(data)
    cut = int(len(s) * proportion)
    return mean(s[cut:len(s) - cut])


def percentile(data, p):
    """p-th percentile (0-100) with linear interpolation."""
    s = sorted(data)
    index = (len(s) - 1) * p / 100
    low, high = math.floor(index), math.ceil(index)
    return s[low] + (s[high] - s[low]) * (index - low)


quartiles = lambda data: (percentile(data, 25), percentile(data, 50), percentile(data, 75))
interquartile_range = lambda data: percentile(data, 75) - percentile(data, 25)
five_number_summary = lambda data: (min(data), percentile(data, 25), percentile(data, 50), percentile(data, 75), max(data))


def outliers_iqr(data):
    """Values more than 1.5 * IQR outside the quartiles."""
    q1, q3 = percentile(data, 25), percentile(data, 75)
    spread = 1.5 * (q3 - q1)
    return [x for x in data if x < q1 - spread or x > q3 + spread]


def exponential_moving_average(data, alpha):
    """Exponential moving average with smoothing factor alpha (0-1)."""
    result = [data[0]]
    for x in data[1:]:
        result.append(alpha * x + (1 - alpha) * result[-1])
    return result


def standardize(data):
    """Rescales data to mean 0 and (sample) standard deviation 1."""
    m, s = mean(data), std_dev_sample(data)
    return [(x - m) / s for x in data]


def spearman_correlation(xs, ys):
    """Rank correlation (ties share the average rank)."""
    def ranks(values):
        order = sorted(range(len(values)), key=lambda i: values[i])
        result = [0.0] * len(values)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
                j += 1
            for k in range(i, j + 1):
                result[order[k]] = (i + j) / 2 + 1
            i = j + 1
        return result
    return pearson_correlation(ranks(xs), ranks(ys))


def linear_regression(xs, ys):
    """Least-squares line -> (slope, intercept, r)."""
    mx, my = mean(xs), mean(ys)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sxx = sum((x - mx) ** 2 for x in xs)
    slope_ = sxy / sxx
    return slope_, my - slope_ * mx, pearson_correlation(xs, ys)


def polynomial_fit(xs, ys, degree):
    """Least-squares polynomial of the given degree -> coefficients, highest power first."""
    size = degree + 1
    normal = [[sum(x ** (i + j) for x in xs) for j in range(size)] for i in range(size)]
    rhs = [sum(y * x ** i for x, y in zip(xs, ys)) for i in range(size)]
    return matrix_solve(normal, rhs)[::-1]


# --- Probability ---
probability = lambda favourable, total: favourable / total
probability_complement = lambda p: 1 - p
probability_union = lambda p_a, p_b, p_a_and_b: p_a + p_b - p_a_and_b
probability_and_independent = lambda p_a, p_b: p_a * p_b
probability_conditional = lambda p_a_and_b, p_b: p_a_and_b / p_b
bayes_theorem = lambda p_b_given_a, p_a, p_b: p_b_given_a * p_a / p_b
bayes_theorem_total = lambda p_b_given_a, p_a, p_b_given_not_a: p_b_given_a * p_a / (p_b_given_a * p_a + p_b_given_not_a * (1 - p_a))
odds_from_probability = lambda p: p / (1 - p)
probability_from_odds = lambda odds: odds / (1 + odds)
birthday_collision_probability = lambda people, days=365: 1 - math.prod((days - i) / days for i in range(people))
expected_trials_geometric = lambda p: 1 / p

# --- Distributions ---
binomial_pmf = lambda n, k, p: math.comb(n, k) * p ** k * (1 - p) ** (n - k)
binomial_cdf = lambda n, k, p: sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k + 1))
binomial_mean = lambda n, p: n * p
binomial_variance = lambda n, p: n * p * (1 - p)
geometric_pmf = lambda k, p: (1 - p) ** (k - 1) * p
geometric_cdf = lambda k, p: 1 - (1 - p) ** k
negative_binomial_pmf = lambda k, r, p: math.comb(k - 1, r - 1) * p ** r * (1 - p) ** (k - r)
hypergeometric_pmf = lambda population, successes, draws, k: math.comb(successes, k) * math.comb(population - successes, draws - k) / math.comb(population, draws)
poisson_pmf = lambda k, lam: (math.exp(-lam) if k == 0 else math.exp(-lam + k * math.log(lam) - math.lgamma(k + 1))) if lam > 0 else (1.0 if k == 0 else 0.0)
poisson_cdf = lambda k, lam: sum(poisson_pmf(i, lam) for i in range(k + 1))
normal_pdf = lambda x, mu=0.0, sigma=1.0: math.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * math.sqrt(TAU))
normal_cdf = lambda x, mu=0.0, sigma=1.0: 0.5 * math.erfc(-(x - mu) / (sigma * SQRT2))
z_score = lambda x, mu, sigma: (x - mu) / sigma
lognormal_pdf = lambda x, mu, sigma: math.exp(-((math.log(x) - mu) ** 2) / (2 * sigma ** 2)) / (x * sigma * math.sqrt(TAU))
exponential_pdf = lambda x, lam: lam * math.exp(-lam * x) if x >= 0 else 0.0
exponential_cdf = lambda x, lam: 1 - math.exp(-lam * x) if x >= 0 else 0.0
uniform_pdf = lambda x, a, b: 1 / (b - a) if a <= x <= b else 0.0
uniform_cdf = lambda x, a, b: 0.0 if x < a else (1.0 if x > b else (x - a) / (b - a))
gamma_pdf = lambda x, shape, scale: x ** (shape - 1) * math.exp(-x / scale) / (math.gamma(shape) * scale ** shape)
beta_pdf = lambda x, a, b: x ** (a - 1) * (1 - x) ** (b - 1) / beta_function(a, b)
chi_square_pdf = lambda x, k: x ** (k / 2 - 1) * math.exp(-x / 2) / (2 ** (k / 2) * math.gamma(k / 2))
student_t_pdf = lambda x, df: math.gamma((df + 1) / 2) / (math.sqrt(df * PI) * math.gamma(df / 2)) * (1 + x * x / df) ** (-(df + 1) / 2)
weibull_pdf = lambda x, shape, scale: (shape / scale) * (x / scale) ** (shape - 1) * math.exp(-((x / scale) ** shape)) if x >= 0 else 0.0
weibull_cdf = lambda x, shape, scale: 1 - math.exp(-((x / scale) ** shape)) if x >= 0 else 0.0
cauchy_pdf = lambda x, x0=0.0, gamma_=1.0: 1 / (PI * gamma_ * (1 + ((x - x0) / gamma_) ** 2))
cauchy_cdf = lambda x, x0=0.0, gamma_=1.0: 0.5 + math.atan((x - x0) / gamma_) / PI
laplace_pdf = lambda x, mu=0.0, b=1.0: math.exp(-abs(x - mu) / b) / (2 * b)
laplace_cdf = lambda x, mu=0.0, b=1.0: 0.5 * math.exp((x - mu) / b) if x < mu else 1 - 0.5 * math.exp(-(x - mu) / b)


def normal_quantile(p, mu=0.0, sigma=1.0):
    """Inverse of the normal CDF: the x where P(X <= x) = p."""
    if not 0 < p < 1:
        raise ValueError("p must be strictly between 0 and 1")
    if p == 0.5:
        return mu
    if p > 0.5:
        return mu - sigma * normal_quantile(1 - p)
    low, high = -40.0, 0.0
    for _ in range(200):
        mid = (low + high) / 2
        if 0.5 * math.erfc(-mid / SQRT2) < p:
            low = mid
        else:
            high = mid
    return mu + sigma * (low + high) / 2


# --- Inference ---
margin_of_error = lambda z, sigma, n: z * sigma / math.sqrt(n)
sample_size_mean = lambda z, sigma, margin: math.ceil((z * sigma / margin) ** 2)
sample_size_proportion = lambda z, p, margin: math.ceil(z * z * p * (1 - p) / margin ** 2)
confidence_interval_mean = lambda sample_mean, sigma, n, confidence=0.95: (sample_mean - normal_quantile((1 + confidence) / 2) * sigma / math.sqrt(n), sample_mean + normal_quantile((1 + confidence) / 2) * sigma / math.sqrt(n))
confidence_interval_proportion = lambda p_hat, n, confidence=0.95: (p_hat - normal_quantile((1 + confidence) / 2) * math.sqrt(p_hat * (1 - p_hat) / n), p_hat + normal_quantile((1 + confidence) / 2) * math.sqrt(p_hat * (1 - p_hat) / n))
t_statistic_one_sample = lambda sample_mean, mu0, s, n: (sample_mean - mu0) / (s / math.sqrt(n))
t_statistic_welch = lambda m1, s1, n1, m2, s2, n2: (m1 - m2) / math.sqrt(s1 * s1 / n1 + s2 * s2 / n2)
z_test_proportion = lambda p_hat, p0, n: (p_hat - p0) / math.sqrt(p0 * (1 - p0) / n)
chi_square_statistic = lambda observed, expected: sum((o - e) ** 2 / e for o, e in zip(observed, expected))
cohens_d = lambda m1, s1, n1, m2, s2, n2: (m1 - m2) / math.sqrt(((n1 - 1) * s1 * s1 + (n2 - 1) * s2 * s2) / (n1 + n2 - 2))

# --- Finance ---
simple_interest = lambda principal, rate, years: principal * rate * years
compound_amount = lambda principal, rate, times_per_year, years: principal * (1 + rate / times_per_year) ** (times_per_year * years)
compound_interest = lambda principal, rate, times_per_year, years: compound_amount(principal, rate, times_per_year, years) - principal
continuous_compound = lambda principal, rate, years: principal * math.exp(rate * years)
present_value = lambda future_value, rate, periods: future_value / (1 + rate) ** periods
future_value = lambda present_value_, rate, periods: present_value_ * (1 + rate) ** periods
future_value_annuity = lambda payment, rate, periods: payment * ((1 + rate) ** periods - 1) / rate
present_value_annuity = lambda payment, rate, periods: payment * (1 - (1 + rate) ** -periods) / rate
future_value_annuity_due = lambda payment, rate, periods: payment * ((1 + rate) ** periods - 1) / rate * (1 + rate)
present_value_annuity_due = lambda payment, rate, periods: payment * (1 - (1 + rate) ** -periods) / rate * (1 + rate)
perpetuity_value = lambda payment, rate: payment / rate
growing_perpetuity_value = lambda payment, rate, growth: payment / (rate - growth)
loan_payment = lambda principal, rate, periods: principal / periods if rate == 0 else principal * rate / (1 - (1 + rate) ** -periods)
loan_balance = lambda principal, rate, periods, payments_made: principal * (1 + rate) ** payments_made - loan_payment(principal, rate, periods) * ((1 + rate) ** payments_made - 1) / rate
loan_total_interest = lambda principal, rate, periods: loan_payment(principal, rate, periods) * periods - principal
effective_annual_rate = lambda nominal_rate, times_per_year: (1 + nominal_rate / times_per_year) ** times_per_year - 1
nominal_rate_from_effective = lambda effective_rate, times_per_year: times_per_year * ((1 + effective_rate) ** (1 / times_per_year) - 1)
real_interest_rate = lambda nominal_rate, inflation: (1 + nominal_rate) / (1 + inflation) - 1             # Fisher equation
rule_of_72 = lambda rate_percent: 72 / rate_percent
cagr = lambda beginning, ending, years: (ending / beginning) ** (1 / years) - 1
roi = lambda gain, cost: (gain - cost) / cost * 100
npv = lambda rate, cash_flows: sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows))
depreciation_straight_line = lambda cost, salvage, life_years: (cost - salvage) / life_years
depreciation_declining_balance = lambda cost, rate, year: cost * (1 - rate) ** (year - 1) * rate
break_even_units = lambda fixed_costs, price, variable_cost: fixed_costs / (price - variable_cost)
markup_price = lambda cost, markup_percent: cost * (1 + markup_percent / 100)
margin_percent = lambda price, cost: (price - cost) / price * 100
discount_price = lambda price, discount_percent: price * (1 - discount_percent / 100)
price_with_tax = lambda price, tax_percent: price * (1 + tax_percent / 100)
tip_amount = lambda bill, tip_percent: bill * tip_percent / 100


def irr(cash_flows, low=-0.9999, high=10.0):
    """Internal rate of return: the rate where the net present value is zero."""
    return bisection(lambda rate: npv(rate, cash_flows), low, high)


# --- Formula Finder ---
def list_formulas(prefix=""):
    """Lists every function whose name starts with `prefix`, e.g. list_formulas("circle_")."""
    found = []
    for name, fn in sorted(globals().items()):
        if name.startswith(prefix) and not name.startswith("_") and name != "main" and callable(fn) and hasattr(fn, "__code__"):
            arguments = ", ".join(fn.__code__.co_varnames[:fn.__code__.co_argcount])
            found.append(f"{name}({arguments})")
    return found


# Help text for the `circle` command used in main()
circleh = "CIRCLE FORMULAS\n" + "\n".join(list_formulas("circle_"))
# ======================================================================
#  END OF MATH FORMULA LIBRARY
# ======================================================================


def main():
    input_list = []
    while True:
        try:
            opening = int(input("""
    THE ULTIMATE PYCULATOR
    1) Get Started
    2) Start Calculating
            """))
        except ValueError:
            pass
        else:
            if opening == 1:
                print(""" 

                """)
            elif opening == 2:
                while True:
                    try:
                        user = input()
                        user = check_float_int(user)
                        for c in user:
                            if c:
                                input_list.append(c)
                        if user is str:
                            user = user.lower().strip()
                            if 'circle' == user:
                                property = input().lower().strip()
                                match property:
                                    case 'help' | '--help':
                                        print(circleh)
                                    case 'r':
                                        user_input_as_list = []
                                        try:
                                            get_user = input()
                                            for index, character in enumerate(get_user):
                                                if character:
                                                    try:
                                                        character = float(character)
                                                    except ValueError:
                                                        character = character.lower
                                                    user_input_as_list.append(character)

                                        except (IndexError, ValueError):

                                    case 'd':
                            elif '=' in input_list:
                                index_start = 0
                                num = []
                                for i, c in enumerate(input_list):
                                    if c == "=":
                                        num1 = int(''.join(input_list[index_start:i]))
                                        index = i
                                        num1 = int(num1)
                                    elif c == "+":
                                        num1 = int(''.join(input_list[index_start:i]))
                                    elif c == '-':
                                        num.append(int(''.join(input_list[index_start:i])))
                                                                        
                                    

def check_float_int(string) -> str:
    """
    Takes 1 arguments, 1 string.
    String type MUST be a str.
    """
    try:
        fi = float(string)
    except ValueError:
        try:
            fi = int(string)
        except ValueError:
            return string
        else:
            return fi
    else:
        return fi

def simply_calculate(number_1: int | float, number_2: int | float, operator: str | None = None):
    """
    Takes 3 arguments, 2 number and 1 for operator.
    Operator MUST be the followings:
        '+' | '-' | '/' | '*'
    If operator None, all operation will be run. 
    """
    try:
        if operator is None:
            return add(number_1, number_2), subtract(number_1, number_2), divide(number_1, number_2), multiply(number_1, number_2)
        elif operator is not None:
            match operator:
                case '+':
                    return add(number_1, number_2)
                case '-':
                    return subtract(number_1, number_2)
                case '/':
                    return divide(number_1, number_2)
                case '*':
                    return multiply(number_1, number_2)
        else:
            raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError
    except ValueError:
        raise ValueError

if __name__ == "__main__":
    main()