# Section F: Analysis

This folder contains the complete written analysis and theoretical justifications answering all six questions from Section F of the lab worksheet.

### Main File:
- [`section_f_analysis.md`](section_f_analysis.md): Complete analysis with mathematical formulas, recurrence relations, and empirical citations from Section D and Section E experiments.

### Summary of Questions Covered:
1. **Sorted vs Random Performance:** Quick Sort degradation ($\sim 75\times$ slower) due to unbalanced partitions; Selection/Merge/Heap invariance; Bubble/Insertion $O(n)$ speedup.
2. **Reverse-Sorted Simple Sorts:** Comparison of Bubble Sort, Selection Sort, and Insertion Sort explaining why Selection Sort is fastest (only $O(n)$ swaps) and Bubble Sort is slowest ($O(n^2)$ tuple swaps).
3. **Merge Sort vs Quick Sort:** Architectural differences between value-agnostic splitting ($O(n \log n)$ guaranteed) vs data-dependent partitioning with last-element pivot ($O(n^2)$ worst case).
4. **Radix Sort Evaluation:** Non-comparison linear time $O(d(n+k))$ vs limitations on non-integers, huge value ranges (large $d$), and auxiliary space.
5. **Search Engine Simulator Evaluation:** Logarithmic $O(\log n)$ Binary Search vs expected $O(1)$ Hash Tables with step counts.
6. **Separate Chaining vs Linear Probing at High Load:** Mathematical demonstration of catastrophic primary clustering in Linear Probing ($50.5$ probes expected at $\alpha = 0.90$) vs graceful degradation in Separate Chaining ($1.45$ comparisons).

