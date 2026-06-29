# cutpointpy
____________
A Python package for estimating the optimal cut-point of a predictor variable (feature) for a binary classification task. It is loosely inspired by [`cutpointr`](https://cran.r-project.org/web/packages/cutpointr/index.html), an optimal cut-point calculation package for [R](https://www.r-project.org/).

Main usage:

 - Optimal cut-point estimation
 - Stability analysis of the estimated cut-points through bootstrapping
 - Receiver-operating characteristic curve (ROC) analysis  

## Installation
`pip install cutpointpy`

## Structure
  - `cutpointpy.core`: contains the main class (`CutpointCalculator`) with functions `find()` and `bootstrap()` respectively for optimal cut-point estimation and stability analysis/validation through bootstrapping.
  - `cutpointpy.utils`: contains ancillary functions including methods for computing performance parameters on binary classification tasks (e.g. confusion matrices, accuracy, sensitivity, specificity and AUC)

## Usage
We recommend the following [marimo](https://marimo.io/) notebooks to get started with `cutpointpy`.
- Optimal cut-point estimation without bootstrapping
    * [cutpointfind__glucose_cutoff_for_diabetes.py](https://molab.marimo.io/notebooks/nb_P81opF6FjJpcwDeycTAVDb)
    * [cutpointfind__ibmi_cutoff_for_diabetes.py](https://molab.marimo.io/notebooks/nb_D5qnT3WHLxrNVpFtwxBHpc)
- Optimal cut-point estimation with bootstrapping
    * [cutpointboot__glucose_cutoff_for_diabetes.py](https://molab.marimo.io/notebooks/nb_ZxGQFfmRsEBb5LRq8hqrXo)


## References
1. Baratloo, A., Hosseini, M., Negida, A., El Ashal, G. [Part 1: simple definition and calculation of accuracy, sensitivity and specificity](https://pmc.ncbi.nlm.nih.gov/articles/PMC4614595/) (2015) Emergency 3(2):48-49
2. Hassanzad M., Hajian-Tilaki K. [Methods of determining optimal cut-point of diagnostic biomarkers with application of clinical data in ROC analysis: an update review](https://doi.org/10.1186/s12874-024-02198-2) (2024) BMC Medical Research Methodology, 24(1), art. no. 84

## Contacts
[Francesco Bianconi](www.bianconif.net) - [bianco@ieee.org](mailto:bianco@ieee.org).
