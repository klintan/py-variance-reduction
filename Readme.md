# Variance reduction for Decision Trees Regression split evaluation

This function computes the relative variance reduction score associated with each split on the targets values. Similar to what is done in sklearn and DecisionTreeRegressor (mse criterion):

It is used in other 
It expects the input to be panda dataframes (y, yleft and yright). Returns score as a float value.

Inputs :
y         = full pandas dataset y values

yleft     = split left group y dataframe

yright     = split right group y dataframe

Outputs :
scores    = relative variance reduction associated with each split


This module and function has been derived from https://github.com/rtaormina/MATLAB_ExtraTrees/blob/master/Functions/Regression/computeScores_r.m

For any improvements of this module feel free to do a pull request.


## Installation
`python setup.py install`

## Usage
```
from py_variance_reduction.vr import VarianceReduction

vr = VarianceReduction()

vr.compute_score(...)
```

