# Section E: Applications

This folder contains practical real-world applications of sorting, binary search, and hashing techniques.

### Files:
1. [`program7_student_records.py`](program7_student_records.py):
   - **Student Record Manager:** Stores student records (roll number, name, marks).
   - **Sorting:** Allows sorting records by roll number, name, or marks using any of the 6 algorithms.
   - **Binary Search:** Searches student by roll number after validating that records are sorted by roll number.
   - **Comparative Report:** Times all 6 algorithms on the student dataset and reports fastest, slowest, and difference.
   - **Run:**
     - Demo Mode: `python program7_student_records.py`
     - Interactive Menu: `python program7_student_records.py --interactive`

2. [`program8_search_engine.py`](program8_search_engine.py):
   - **Search Engine Simulator:** Stores a CS vocabulary dictionary of 35 words mapped to document IDs and term frequencies.
   - **Lookups Implemented:**
     1. Binary Search on sorted word list ($O(\log n)$)
     2. Hash Table with Separate Chaining ($O(1)$)
     3. Hash Table with Linear Probing ($O(1)$)
   - **Feature:** Reports whether the query is found and outputs the exact number of comparisons/probes required by each method.
   - **Run:**
     - Demo Mode: `python program8_search_engine.py`
     - Interactive Search: `python program8_search_engine.py --interactive`

