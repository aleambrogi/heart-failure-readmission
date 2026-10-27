# Historical results and interpretation

## Task and analysis

The group explored prediction of readmission within six months using demographic,
laboratory, comorbidity, medication and echocardiographic variables. The original analysis
includes data consistency checks, exclusion of deaths, removal of future-outcome predictors,
missingness indicators, iterative imputation with a random-forest estimator, feature
engineering, Elastic Net / Boruta selection and model comparisons.

## Saved original results

These numbers were extracted from the original notebook's stored outputs before clearing
them for publication. They have **not** been independently reproduced in this edition.
The resulting model inputs had 1,556 training and 390 test observations.

| Model | Test ROC-AUC |
|---|---:|
| Weighted logistic regression with forward selection | 0.685134 |
| RBF support vector machine | 0.675525 |
| Stacking | 0.666054 |
| Soft voting | 0.665065 |
| XGBoost | 0.652711 |

For the selected logistic regression, saved test F1 was **0.5816**, sensitivity **0.6323**,
specificity **0.6426** and precision **0.5385**, using a 0.5 classification threshold.
The saved feature-selection output records 19 consensus and 67 union predictors; the
forward-selection model retains 36 predictors. The original report lists a smaller set of
highlighted predictors, so it should not be read as the exact final model specification.

The project illustrates a useful modelling trade-off: a simpler, interpretable classifier
was competitive with the more complex alternatives on this particular split.

## Limitations that matter

- **Single-centre retrospective data:** no external or prospective validation.
- **Exploratory holdout use:** several models were compared on the same test split;
  choosing a model from those scores weakens the interpretation of the holdout as a
  completely untouched final estimate.
- **Preprocessing outside internal CV:** imputation and initial feature selection are
  fitted on the training set before downstream model CV. Thus internal CV does not
  validate the entire preprocessing/selection workflow. A stronger evaluation would
  refit all learned transformations inside each fold and use nested model selection.
- **Whole-cohort exploration:** some cleaning / engineering choices were informed by
  exploratory analysis before the split. A stricter study would predefine these rules or
  learn them within the training folds.
- **Survivor conditioning:** excluding people who died during follow-up conditions the
  task on future survival. Death does not imply that no earlier readmission occurred.
  A deployable discharge-time model would need an explicit competing-risk / outcome
  definition and appropriate handling of death and censoring.
- **Imputation terminology:** the notebook uses a single `IterativeImputer` completion
  with a random-forest estimator; this is not a pooled multiple-imputation analysis.
- **Reproducibility:** the original environment was not recorded. Some feature-list
  ordering and random forward-selection shuffling are unseeded, and the Optuna study
  is not fully seeded. Exact metrics can change on a fresh run.
- **Interpretation is associational:** coefficients and SHAP values explain model
  behaviour; they do not establish causal effects or clinical recommendations.

The public notebook preserves the original academic modelling choices rather than silently
replacing them and continuing to claim the original scores. A future methodological revision
would require a fresh evaluation and separate results.
