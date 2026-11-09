<div align="center">

# SECTION E

**Practical Applications**

![Section](https://img.shields.io/badge/DAA_LAB-SECTION%20E-17243A?style=for-the-badge)
![Focus](https://img.shields.io/badge/Design-Vintage%20Academic%20%2B%20Modern-2A7F78?style=flat-square)

</div>

---

## Overview

This folder contains practical real-world applications of sorting, binary search, and hashing techniques.

## Application Directory

### 01 · Student Record Manager

**File:** [`program7_student_records.py`](program7_student_records.py)

- **Purpose:** Stores student records containing roll number, name, and marks.
- **Sorting:** Sorts records by roll number, name, or marks using any of the six algorithms.
- **Binary Search:** Searches for a student by roll number after validating that records are sorted by roll number.
- **Comparative Report:** Times all six algorithms on the student dataset and reports the fastest, slowest, and time difference.

**Run options:**

```bash
# Demo mode
python program7_student_records.py

# Interactive menu
python program7_student_records.py --interactive
```

### 02 · Search Engine Simulator

**File:** [`program8_search_engine.py`](program8_search_engine.py)

- **Purpose:** Stores a CS vocabulary dictionary of 35 words mapped to document IDs and term frequencies.
- **Lookup methods:**
  1. Binary Search on a sorted word list — `O(log n)`
  2. Hash Table with Separate Chaining — `O(1)`
  3. Hash Table with Linear Probing — `O(1)`
- **Feature:** Reports whether a query is found and outputs the exact number of comparisons or probes required by each method.

**Run options:**

```bash
# Demo mode
python program8_search_engine.py

# Interactive search
python program8_search_engine.py --interactive
```

## At a Glance

| Application | Main concepts |
|:--|:--|
| Student Record Manager | Sorting, Binary Search, comparative timing |
| Search Engine Simulator | Binary Search, Separate Chaining, Linear Probing |

---

<div align="center">

*DAA Laboratory · Section E*

</div>
