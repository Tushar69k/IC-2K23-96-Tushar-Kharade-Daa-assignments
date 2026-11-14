# DAA_LAB_IIPS
NOTE- assignment of different days in specific folders 

# DAA Lab Repository

This repository contains my Design Analysis and Algorithms lab assignments. The work here tracks my progress from basic control structures and step counting to advanced algorithms, data structures, and empirical performance analysis.

## Folder Structure

* `lab_1/` : Contains introductory logic tasks, loop analysis, and basic data structures.
* `lab_2/` : Contains implementations of 1D/2D array operations, sparse matrices, and a matrix calculator.
* `lab_3/` : Contains advanced sorting, searching, hash tables, and real-world application simulations.
* `Coursework/` : Contains 15 comprehensive algorithm implementations mapping directly to university Course Outcomes (CO1-CO5).

## Brief Overview of Programs

### Lab 1: Fundamentals and Step Counting
* Traced how to manually find the largest number in a list and counted the exact number of comparisons needed.
* Implemented Stacks (Last-In-First-Out) and Queues (First-In-First-Out) to understand how task scheduling and printer jobs handle data differently.
* Analyzed single and nested loops to understand how the number of execution steps grows proportionally or explosively as input size increases.

### Lab 2: Arrays and Matrices
* **1D Array Operations (`array_operations_1d.py`):** Implemented insertion, deletion, linear search, and left/right rotation using modulo slicing. Includes strict boundary and index validation.
* **2D Array Operations (`array_operations_2d.py`):** Handled row insertion/deletion, 2D value searching, and 90-degree clockwise matrix rotation using coordinate mapping (`[r][c]` to `[c][rows - 1 - r]`).
* **Sparse Matrix (`sparse_matrix.py`):** Converted full matrices to `(row, col, value)` triples. Implemented sparse matrix addition using a two-pointer merge approach that successfully identifies and cancels out zero-sum entries.
* **Matrix Calculator (`matrix_calculator.py`):** Built a menu-driven calculator supporting addition, multiplication, transposition, and recursive determinant calculation with strict dimension validation.
* **Space Complexity Analysis:** Evaluated the memory cutoff point for sparse matrices. Documented that a sparse representation ($3k$ values) stops saving memory compared to a full matrix ($m \times n$ values) when non-zero elements exceed ~33.3%. This makes sparse matrices highly efficient for real-world applications like social network graphs.

### Lab 3: Algorithms and Performance Analysis
* Wrote basic $O(n^2)$ sorting algorithms: Bubble Sort, Selection Sort, and Insertion Sort.
* Wrote advanced $O(n \log n)$ sorting algorithms: Merge Sort, Quick Sort, and Heap Sort.
* Implemented Radix Sort for integers and an iterative Binary Search for sorted arrays.
* Generated large datasets (random, sorted, reverse-sorted) to time every sorting algorithm and graph the performance differences.
* Developed a Student Record Manager that sorts and searches a database of students by roll number, name, and marks.
* Built a Search Engine Simulator to compare the lookup efficiency of Binary Search against Hash Tables (implementing both Separate Chaining and Linear Probing for collision handling).
* Documented a full theoretical analysis connecting the empirical timing results to their expected algorithmic time complexities.

### Coursework: Advanced Algorithmic Strategies
* **Divide and Conquer:** Implemented recursive and iterative Binary Search, Min/Max finding, and advanced sorting (Quick, Merge, Selection, Insertion, Radix). Includes automated benchmarking, dataset generators, and `matplotlib` performance graphs plotting execution time against input size $n$.
* **The Greedy Strategy:** Solved the Fractional Knapsack problem, Job Sequencing with deadlines, and Minimum Cost Spanning Trees using both Prim’s and Kruskal’s algorithms.
* **Dynamic Programming:** Implemented the 0/1 Knapsack problem and an optimized memoized Fibonacci series.
* **Exhaustive Search & Backtracking:** Implemented Depth First Search (DFS), Breadth First Search (BFS), and the classic 8-Queens Problem.
* **Branch and Bound:** Solved the Traveling Salesperson Problem (TSP) using Dijkstra's algorithm concepts.
* *Note: A dedicated mapping README is included inside this folder detailing how each script aligns with the specific university syllabus questions and CO1-CO5.*
