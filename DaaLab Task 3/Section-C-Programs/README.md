# Section C: Programs to Write

This folder contains standalone implementations of the fundamental sorting algorithms and iterative binary search.

### Files:
1. [`program1_simple_sorts.py`](program1_simple_sorts.py):
   - **Algorithms:** Bubble Sort, Selection Sort, Insertion Sort.
   - **Feature:** Prints array status after each pass or step to make the sorting process visible.
   - **Run:** `python program1_simple_sorts.py`
2. [`program2_advanced_sorts.py`](program2_advanced_sorts.py):
   - **Algorithms:** Merge Sort, Quick Sort, Heap Sort.
   - **Pivot Strategy:** Last element (`pivot = arr[high]`) using Lomuto partitioning.
   - **Run:** `python program2_advanced_sorts.py`
3. [`program3_radix_sort.py`](program3_radix_sort.py):
   - **Algorithm:** Radix Sort (LSD approach for non-negative integers).
   - **Feature:** Helper function for stable Counting Sort called for each digit place ($1, 10, 100, \dots$).
   - **Run:** `python program3_radix_sort.py`
4. [`program4_binary_search.py`](program4_binary_search.py):
   - **Algorithm:** Iterative Binary Search.
   - **Feature:** Returns index of target or -1 if not found. Tested on existing and non-existing values.
   - **Run:** `python program4_binary_search.py`

