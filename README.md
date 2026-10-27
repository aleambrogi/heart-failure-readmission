# Heart failure readmission prediction

**Interpretable statistical learning on clinical data** · Collaborative university project

Predicting hospital readmission within six months for patients with heart failure, using the
Heart Failure Zigong database. The project compares logistic regression, XGBoost, support
vector machines and ensemble methods, with particular attention to missing values,
feature selection and interpretability.

**Authors:** Mattia Alborghetti, Alessandro Ambrogi and Francesco Colombo.  
**Course:** Statistical Learning for Healthcare Data, Politecnico di Milano.

## At a glance

- Python: pandas, scikit-learn, XGBoost, Optuna, Boruta and SHAP.
- Data quality checks, missingness analysis and clinically motivated feature engineering.
- Iterative imputation, Elastic Net / Boruta feature selection and stratified cross-validation.
- Historical held-out ROC-AUC **0.6851** for the selected weighted logistic regression;
  **F1 0.5816**, on 390 test observations. These are saved original results, not a new rerun.
- Interpretation through coefficients, SHAP and exploratory subgroup comparisons.

This is an educational research project. The evaluation has limitations documented in
[RESULTS.md](RESULTS.md); it does not establish clinical usefulness or readiness for deployment.

## Repository contents

| File | Purpose |
|---|---|
| [HF_Project.ipynb](HF_Project.ipynb) | Original analysis with portable input paths and all outputs cleared |
| [RESULTS.md](RESULTS.md) | Aggregate historical results and methodological limitations |
| [DATA_ACCESS.md](DATA_ACCESS.md) | Data source, access procedure and redistribution restrictions |
| [requirements.txt](requirements.txt) | Dependencies for the analysis; not a historically locked environment |
| [check_project.py](check_project.py) | Standard-library structural and optional local-input checks |
| [CREDITS.md](CREDITS.md) | Authorship, data citations and portfolio-edit scope |

## Run locally

Python 3.11 or 3.12 is recommended as a starting environment; the complete dependency set
has not been installed and tested for this portfolio edition.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS / Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python check_project.py
```

Obtain the data directly from PhysioNet, accept its terms yourself, and place the authorized
`dat.csv` and `dat_md.csv` files in a local `data/` folder. That folder is ignored by Git.
Alternatively set `HF_DATA_DIR` to an existing private directory:

```powershell
$env:HF_DATA_DIR = 'C:/private/zigong'
python check_project.py --data-dir $env:HF_DATA_DIR
jupyter lab HF_Project.ipynb
```

On macOS/Linux use `export HF_DATA_DIR=/private/zigong`. Run notebook cells from top to
bottom using the activated environment. Feature selection, iterative imputation and
hyperparameter optimisation can take substantial time and use multiple CPU cores.
Outputs can contain patient-level information: keep executed notebooks private and
clear every output before committing.

## Verification status

The public notebook's Python cells were parsed successfully, all stored outputs and student
numbers were removed, and both local input schemas were checked without publishing rows.
The full training / tuning / SHAP workflow has **not** been rerun in the portfolio environment.
See RESULTS.md for why the historical evaluation should be read as exploratory.

## Data and rights

**No clinical CSVs, fitted models or patient-level outputs are included.** PhysioNet lists this
dataset as restricted access under the Restricted Health Data License and Data Use Agreement.
Download it from the [official dataset page](https://physionet.org/content/heart-failure-zigong/1.3/).
Local reference-paper PDFs are not redistributed. The original report is retained locally;
the public summary uses the notebook's aggregate metrics and makes its limitations explicit.

The project remains joint work of the three authors. No blanket open-source licence is
asserted for jointly authored material; contact the authors about reuse. Dataset rights are
separate and remain governed by PhysioNet's terms.
