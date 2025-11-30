# Math2011 – Programming for Math and Science

This repository contains Python-based solutions, algorithms, and numerical methods developed as part of the **MATH2011: Programming for Mathematics and Science** university course.

The code showcases applied mathematical programming using clean, modular Python, with a focus on real-world computation techniques, linear algebra, numerical methods, and more.

> ✅ All scripts were executed and verified in **Visual Studio Code**, using Python’s module system (e.g., `py -m linear_algebra.vector_geometry_3d`).

---

## 🧠 Project Structure

| Folder | Description |
|--------|-------------|
| `algorithms/` | Classic algorithm problems and CS fundamentals – includes recursion, anagram checks, Pascal’s triangle, and logical operators. |
| `linear_algebra/` | Modular implementations of vector and matrix operations, decomposition methods (LU, QR), custom `Matrix` and `Vector` classes, and 3D geometry. |
| `numeric_methods/` | Numerical analysis methods such as root finding, minimization, interpolation, and floating point comparison. |
| `misc/` | Additional utilities and course-specific assignments, including grid rendering, moduli calculations, a gradient path optimizer, and even a mathematical poem generator. |

---

## 🚀 How to Run

All files are standalone **except** for `linear_algebra/`, where modules are interconnected and should be run as packages.

### 🧪 Example:
```bash
# Run a standalone algorithm script
py -m algorithms.anagram

# Run a linear algebra module that depends on other files
py -m linear_algebra.vector_geometry_3d
```

---

## 📦 Dependencies

Make sure the following packages are installed (via `pip` or your environment manager):

```bash
pip install numpy matplotlib
```

### Also uses:
- `math` (standard lib)
- `copy` (standard lib)
- `collections` (standard lib)
- `mpl_toolkits.mplot3d` (part of `matplotlib`)

---

## 🧰 Tools Used

- **Language:** Python 3
- **IDE:** Visual Studio Code
- **Modules:** Python packages and internal imports
- **Execution:** Module-based (`py -m path.to.module`)

---

## 📄 License

This project is shared for **educational and portfolio** purposes. Please cite if used.

---

## 💼 About

Created as part of the MATH2011 course, this repository demonstrates practical and theoretical applications of programming in mathematics and science. Designed to be readable, extensible, and useful for students, reviewers, and potential employers.

---

### 🔗 Author

**Lawrence Cook**  
