<div align="center">

# SECTION C

**Programs to Write**

![Section](https://img.shields.io/badge/DAA_LAB-SECTION%20C-17243A?style=for-the-badge)
![Focus](https://img.shields.io/badge/Design-Vintage%20Academic%20%2B%20Modern-2A7F78?style=flat-square)

</div>

---

## Overview

This folder contains standalone implementations of fundamental sorting algorithms and iterative binary search.

## Program Directory

### 01 · Simple Sorting Algorithms

**File:** [`program1_simple_sorts.py`](program1_simple_sorts.py)

- **Algorithms:** Bubble Sort, Selection Sort, Insertion Sort.
- **Feature:** Prints the array status after each pass or step to make the sorting process visible.
- **Run:**
  ```bash
  python program1_simple_sorts.py
  ```

### 02 · Advanced Sorting Algorithms

**File:** [`program2_advanced_sorts.py`](program2_advanced_sorts.py)

- **Algorithms:** Merge Sort, Quick Sort, Heap Sort.
- **Pivot strategy:** Last element (`pivot = arr[high]`) using Lomuto partitioning.
- **Run:**
  ```bash
  python program2_advanced_sorts.py
  ```

### 03 · Radix Sort

**File:** [`program3_radix_sort.py`](program3_radix_sort.py)

- **Algorithm:** Radix Sort (LSD approach for non-negative integers).
- **Feature:** Uses a stable Counting Sort helper for each digit place (`1, 10, 100, ...`).
- **Run:**
  ```bash
  python program3_radix_sort.py
  ```

### 04 · Iterative Binary Search

**File:** [`program4_binary_search.py`](program4_binary_search.py)

- **Algorithm:** Iterative Binary Search.
- **Feature:** Returns the index of the target or `-1` if it is not found. Tested on existing and non-existing values.
- **Run:**
  ```bash
  python program4_binary_search.py
  ```

---

## At a Glance

| Program | Core concepts |
|:--|:--|
| `program1_simple_sorts.py` | Bubble, Selection, Insertion Sort |
| `program2_advanced_sorts.py` | Merge, Quick, Heap Sort |
| `program3_radix_sort.py` | LSD Radix Sort and stable Counting Sort |
| `program4_binary_search.py` | Iterative Binary Search |

---

<div align="center">

*DAA Laboratory · Section C*

</div>
