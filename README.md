# NAVTTC AI/ML — Weeks 1 to 5 (Python + VS Code)

This beginner-friendly practice pack follows the main topics in the uploaded NAVTTC outline for Weeks 1–5:
- Week 1: Python basics, strings, input/type casting, data structures, conditions, loops
- Week 2: functions, scope, lambda/map/filter, files, exceptions, OOP, descriptive statistics
- Week 3: probability, NumPy arrays and operations, Pandas basics and data cleaning
- Week 4: Pandas joins/grouping/plots, Seaborn, ML pipeline, simple linear regression
- Week 5: multiple linear regression, polynomial regression, binary and multiclass logistic regression

## 1. Open in VS Code
1. Extract the ZIP file.
2. Open the extracted `NAVTTC_Weeks1_to_5_VSCode` folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Create a virtual environment (recommended):

   **Windows**
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, you can still run using `.venv\Scripts\python.exe`, or use Command Prompt:
   ```bat
   .venv\Scripts\activate.bat
   ```

5. Install libraries:
   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

If `python` is not recognized on Windows, try `py` instead.

## 2. Run a lesson
From the project root, run for example:
```bash
python week1_python_basics/01_variables_types.py
python week3_numpy_pandas/01_numpy_arrays.py
python week4_pandas_visualization_ml/04_simple_linear_regression.py
python week5_machine_learning/01_multiple_linear_regression.py
```

In VS Code you can also open a `.py` file and click the ▶ Run Python File button. Make sure the selected interpreter is this project's `.venv`.

## 3. Recommended order
Run the numbered files in each week folder from smallest number to largest number. Read the comments and change the example values to practise.

## Notes
- The examples create small sample datasets themselves, so no extra CSV files are required.
- Plot scripts open a chart window; close it to continue.
- Some topics in the outline (for example, Linux shell commands) are terminal commands, not Python scripts. See `week1_python_basics/linux_commands.md`.
- These are teaching examples, not a replacement for your instructor's exact classroom tasks.
