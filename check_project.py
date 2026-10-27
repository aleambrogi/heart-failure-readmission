"""Structural checks; never trains models or prints patient records."""
import argparse
import ast
import csv
import importlib.util
import json
from pathlib import Path

def check_public_notebook(path):
    nb = json.loads(path.read_text(encoding="utf-8"))
    count = 0
    for i, cell in enumerate(nb["cells"]):
        source = "".join(cell["source"])
        if "Codice persona" in source:
            raise ValueError("Student identifier found")
        if cell["cell_type"] == "code":
            ast.parse(source, filename=f"cell_{i}")
            if cell.get("outputs") or cell.get("execution_count") is not None:
                raise ValueError("Public notebook must have all outputs cleared")
            count += 1
    print(f"Notebook checks passed: {count} Python cells; no stored outputs or student numbers.")

def check_data(directory):
    expected = {
        "dat.csv": {"inpatient.number", "re.admission.within.6.months",
                    "outcome.during.hospitalization", "death.within.6.months"},
        "dat_md.csv": {"inpatient.number", "Drug_name"},
    }
    for name, required in expected.items():
        with (directory / name).open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            missing = required - set(reader.fieldnames or [])
            if missing:
                raise ValueError(f"{name}: missing required columns: {sorted(missing)}")
            count = sum(1 for _ in reader)
        if count == 0:
            raise ValueError(f"{name}: empty file")
        print(f"{name}: required columns present; {count} rows (values withheld).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path)
    args = parser.parse_args()
    check_public_notebook(Path(__file__).with_name("HF_Project.ipynb"))
    if args.data_dir:
        check_data(args.data_dir)
    modules = ["numpy", "pandas", "scipy", "sklearn", "matplotlib", "seaborn",
               "boruta", "xgboost", "optuna", "shap", "interpret"]
    missing = [name for name in modules if importlib.util.find_spec(name) is None]
    print("Missing analysis dependencies: " + ", ".join(missing) if missing else
          "Analysis dependencies detected (imports/training not tested by this check).")
