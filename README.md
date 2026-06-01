# Calx — Scientific Calculator

A desktop calculator application built with Python and CustomTkinter, supporting both basic arithmetic and a full suite of scientific operations including trigonometry, logarithms, matrix algebra, and 3D vector math.

---

## Project Structure

```
CALCULATOR/
├── core/
│   ├── __init__.py
│   ├── basic.py          # Arithmetic operations
│   └── sceintific.py     # Scientific math backend
└── calx_ui.py            # Main application UI
```

---

## Features

### Basic Mode
- Addition, subtraction, multiplication, division
- Percentage calculation
- Decimal input and sign toggle
- Full expression display with live result
- Keyboard support (digits, operators, Enter, Backspace, Escape)

### Advanced Mode (four tabs)

**Trig**
Supports degree and radian input. Functions: sin, cos, tan, arcsin, arccos, arctan.

**Log / Exp**
Functions: natural log, log base 10, log with arbitrary base, power (xʸ), square root, exponential (eˣ), square (x²), percentage.

**Matrix (2×2)**
Operations: addition, subtraction, multiplication, inverse, trace, rank, determinant.

**Vector (3D)**
Operations: addition, subtraction, dot product, cross product, magnitude of u, magnitude of v.

---

## Requirements

- Python 3.9+
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) — modern themed Tkinter widgets
- [NumPy](https://numpy.org/) — matrix and vector computations

Install dependencies:

```bash
pip install customtkinter numpy
```

---

## Running the App

From the project root:

```bash
python calx_ui.py
```

The basic calculator opens immediately. Click **Adv** to launch the Advanced window as a separate panel.

---

## Module Reference

### `core/basic.py`

| Function | Description |
|---|---|
| `addition(a, b)` | Returns a + b |
| `subtraction(a, b)` | Returns a − b |
| `multiplication(a, b)` | Returns a × b |
| `division(a, b)` | Returns a ÷ b |
| `parcentage(a, b)` | Returns (a / b) × 100 |

### `core/sceintific.py`

**`Matrix`** — wraps NumPy array operations

| Method | Description |
|---|---|
| `madd(m1, m2)` | Element-wise addition |
| `msub(m1, m2)` | Element-wise subtraction |
| `matrix_multiplication(m1, m2)` | Matrix product |
| `inverse(m1)` | Matrix inverse |
| `trace(m1)` | Sum of diagonal elements |
| `ma_rank(m1)` | Matrix rank |
| `determinant(m1)` | Determinant of a square matrix |
| `system_of_linear_equation(A, B)` | Solves Ax = B; returns solution type and values |

**`vector`** — 3D vector operations

| Method | Description |
|---|---|
| `vadd(v1, v2)` | Vector addition |
| `vsub(v1, v2)` | Vector subtraction |
| `dot_product(v1, v2)` | Dot product |
| `cross_product(v1, v2)` | Cross product |
| `magnitude(v)` | Euclidean norm |

**`Tignomatry`** — trigonometric functions (input in radians)

`sin_fun`, `cos_fun`, `tangent`, `arcsin`, `arccos`, `arctan`

**`logarthmic`** — logarithm functions

`natural_log(x)`, `log_10(x)`, `log_base(x, base)`

**`expoant`** — exponential and power functions

`power(x, y)`, `square_root(x)`, `square(x)`, `expnantial(x)`

**`angulur_conversion`** — angle unit helpers

`degree_to_radian(deg)`, `radian_to_degree(rad)`

---


## License

MIT License. Free to use, modify, and distribute.
