# cutpointpy
____________
A Python package for estimating the optimal cut-point of a predictor variable (feature) for a binary classification task. It is loosely inspired by [`cutpointr`](https://cran.r-project.org/web/packages/cutpointr/index.html), an optimal cut-point calculation package for [R](https://www.r-project.org/).

The main use cases of `cutpointpy` are:

 - Optimal cut-point estimation
 - Stability analysis of the estimated cut-points through bootstrapping
 - Receiver-operating characteristic curve (ROC) analysis  

## Installation
Coming up soon

## Structure
  - `cutpointpy.core`: contains the main class (`CutpointCalculator`) with functions `find()` and `bootstrap()` for optimal cut-point estimation and stability anslysis/validation through bootstrapping.
  - `cutpointpy.utils`: contains ancillary functions including methods for computing performance parameters on binary classification tasks (e.g. accuracy, sensitivity, specificity and AUC)

## Usage
Coming up soon.  

## References
1. Hassanzad M., Hajian-Tilaki K. [Methods of determining optimal cut-point of diagnostic biomarkers with application of clinical data in ROC analysis: an update review (2024) BMC Medical Research Methodology, 24 (1), art. no. 84](https://doi.org/10.1186/s12874-024-02198-2)

## Note
The package is still under development and not fully tested.
