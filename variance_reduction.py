from __future__ import division

import numpy as np
import pandas as pd

class VarianceReduction():
    """
     This function computes the relative variance reduction score associated
    with each split on the targets values. Similar to what is done in sklearn and DecisionTreeRegressor (mse criterion):

    Inputs :
    y         = full pandas dataset y values
    yleft     = split left group y dataframe
    yright     = split right group y dataframe


    Outputs :
    scores    = relative variance reduction associated with each split


    This module and function has been derived from https://github.com/rtaormina/MATLAB_ExtraTrees/blob/master/Functions/Regression/computeScores_r.m

    Attributes:
        score: The computed score
    """

    def __init__(self):
        """Initialize variance reduction scoring
        """

    def compute_score(self, y, yleft, yright):
        """Computes variance score for split."""

        # get dataset length n and number of attributes nAtt
        n = len(y.index)

        # compute target variance for the dataset
        y_var = y.var()

        # compute target variance for the two branches
        yleft_var = yleft.var()
        yright_var = yright.var()

        nleft = len(yleft.index)
        nright = len(yright.index)

        # compute scores
        scores = (y_var - nleft/n*yleft_var - nright/n*yright_var)/y_var;
        return scores