"""
Master Runner Script: run_all.py
Executes all 8 lab programs sequentially from their respective section directories
to verify and demonstrate the complete structured lab suite.
"""

import subprocess
import sys
import os

SCRIPTS = [
    ("Program 1: Simple Sorts (Bubble, Selection, Insertion)", os.path.join("Section-C-Programs", "program1_simple_sorts.py")),
    ("Program 2: Advanced Sorts (Merge, Quick, Heap)", os.path.join("Section-C-Programs", "program2_advanced_sorts.py")),
    ("Program 3: Radix Sort (LSD Counting Sort)", os.path.join("Section-C-Programs", "program3_radix_sort.py")),
    ("Program 4: Iterative Binary Search", os.path.join("Section-C-Programs", "program4_binary_search.py")),
    ("Program 5: Sorting Comparison Benchmark", os.path.join("Section-D-Timing-Analysis", "program5_sorting_comparison.py")),
    ("Program 6: Performance Graphing (Matplotlib)", os.path.join("Section-D-Timing-Analysis", "program6_graphing.py")),
    ("Program 7: Student Record Manager", os.path.join("Section-E-Applications", "program7_student_records.py")),
    ("Program 8: Search Engine Simulator", os.path.join("Section-E-Applications", "program8_search_engine.py")),
]

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    print("=" * 75)
    print("      DAA LAB TASK 3 - STRUCTURED AUTOMATED VERIFICATION SUITE       ")
    print("=" * 75)

    passed = 0
    failed = 0

    for title, rel_path in SCRIPTS:
        script_full_path = os.path.join(root_dir, rel_path)
        script_working_dir = os.path.dirname(script_full_path)
        script_name = os.path.basename(script_full_path)

        print(f"\n>>> Running {title} [{rel_path}]...")
        print("-" * 75)
        try:
            res = subprocess.run(
                [sys.executable, script_full_path],
                cwd=script_working_dir,
                capture_output=True,
                text=True,
                check=True
            )
            print(res.stdout.strip())
            passed += 1
            print(f"[STATUS] {script_name} PASSED.")
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] {script_name} failed with exit code {e.returncode}:")
            print(e.stderr)
            failed += 1

    print("\n" + "=" * 75)
    print(f"VERIFICATION SUMMARY: {passed}/{len(SCRIPTS)} Programs Passed ({failed} Failed)")
    print("=" * 75)

if __name__ == "__main__":
    main()
