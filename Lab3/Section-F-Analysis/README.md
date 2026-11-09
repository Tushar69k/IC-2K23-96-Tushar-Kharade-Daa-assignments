<div align="center">

# SECTION F

**Analysis & Theoretical Justifications**

![Section](https://img.shields.io/badge/DAA_LAB-SECTION%20F-17243A?style=for-the-badge)
![Focus](https://img.shields.io/badge/Design-Vintage%20Academic%20%2B%20Modern-2A7F78?style=flat-square)

</div>

---

## Overview

This folder contains the complete written analysis and theoretical justifications answering all six questions from Section F of the lab worksheet.

## Main File

| File | Description |
|:--|:--|
| [`section_f_analysis.md`](section_f_analysis.md) | Complete analysis with mathematical formulas, recurrence relations, and empirical citations from the Section D and Section E experiments. |

## Summary of Questions Covered

### F1 · Sorted vs Random Performance

Quick Sort degradation (`~75×` slower) due to unbalanced partitions; Selection, Merge, and Heap Sort invariance; Bubble and Insertion Sort `O(n)` speedup.

### F2 · Reverse-Sorted Simple Sorts

Comparison of Bubble Sort, Selection Sort, and Insertion Sort, explaining why Selection Sort is fastest (only `O(n)` swaps) and Bubble Sort is slowest (`O(n²)` tuple swaps).

### F3 · Merge Sort vs Quick Sort

Architectural differences between value-agnostic splitting (`O(n log n)` guaranteed) and data-dependent partitioning with a last-element pivot (`O(n²)` worst case).

### F4 · Radix Sort Evaluation

Non-comparison linear time `O(d(n + k))` versus limitations on non-integers, huge value ranges (large `d`), and auxiliary space.

### F5 · Search Engine Simulator Evaluation

Logarithmic `O(log n)` Binary Search versus expected `O(1)` Hash Tables, supported by step counts.

### F6 · Separate Chaining vs Linear Probing at High Load

Mathematical demonstration of catastrophic primary clustering in Linear Probing (`50.5` probes expected at `α = 0.90`) versus graceful degradation in Separate Chaining (`1.45` comparisons).

---

<div align="center">

*DAA Laboratory · Section F*

</div>
