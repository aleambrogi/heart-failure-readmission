# Data access

## Source

Zhang, Z., Cao, L., Zhao, Y., Xu, Z., Chen, R., Lv, L., & Xu, P. (2022).
*Hospitalized patients with heart failure: integrating electronic healthcare records and
external outcome data*, version 1.3. PhysioNet.
https://doi.org/10.13026/5m60-vs44

Official page: https://physionet.org/content/heart-failure-zigong/1.3/

The resource contains 2,008 hospital admissions from a single centre in Sichuan, China,
collected during 2016-2019. Access is restricted to registered users who sign the applicable
data-use agreement. It must not be treated as an unrestricted public dataset.

## Local files

1. Register with PhysioNet and complete its required access steps yourself.
2. Download `dat.csv` and `dat_md.csv` directly from the authorised resource.
3. Store them under `data/` or set the `HF_DATA_DIR` environment variable.
4. Run `python check_project.py --data-dir PATH` to check the expected input schemas.

The local course dataset is labelled as Zigong data, but its precise download version has
not been independently established. Version 1.3 is the cited access reference, not a claim
that the local CSVs are byte-identical to that release.

The data dictionary can also be obtained from the source. Do not commit CSVs, intermediate
tables, trained artefacts, patient identifiers, or executed notebooks with row-level outputs.
This repository intentionally supplies no automatic downloader or embedded credentials.
