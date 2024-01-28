# from https://goodboychan.github.io/python/datacamp/machine_learning/2020/06/05/01-School-Budgeting-with-Machine-Learning-in-Python.html
# these functions are used in 2024-01-19_school_budgeting_with_maching_learning_in_python

import pandas as pd
import numpy as np


BOX_PLOTS_COLUMN_INDICES = [range(0, 37), range(37, 48), range(48, 51), range(51, 76), range(76, 79), range(79, 82), range(82, 87), range(87, 96), range(96, 104)]


def _multi_multi_log_loss(predicted, actual, class_column_indices=BOX_PLOTS_COLUMN_INDICES, eps=1e-15):
    """ Multi class version of Logarithmic Loss metric as implemented on
    DrivenData.org
    """
    class_scores = np.ones(len(class_column_indices), dtype=np.float64)
    
    # calculate log loss for each set of columns that belong to a class:
    for k, this_class_indices in enumerate(class_column_indices):
        # get just the columns for this class
        preds_k = predicted[:, this_class_indices].astype(np.float64)
        
        # normalize so probabilities sum to one (unless sum is zero, then we clip)
        preds_k /= np.clip(preds_k.sum(axis=1).reshape(-1, 1), eps, np.inf)

        actual_k = actual[:, this_class_indices]

        # shrink predictions so
        y_hats = np.clip(preds_k, eps, 1 - eps)
        sum_logs = np.sum(actual_k * np.log(y_hats))
        class_scores[k] = (-1.0 / actual.shape[0]) * sum_logs
        
    return np.average(class_scores)
 
 
def score_submission(pred_path='./', holdout_path='https://s3.amazonaws.com/assets.datacamp.com/production/course_2826/datasets/TestSetLabelsSample.csv'):
    # this happens on the backend to get the score
    holdout_labels = pd.get_dummies(
        pd.read_csv(holdout_path, index_col=0)
        .apply(lambda x: x.astype('category'), axis=0)
    )
    
    preds = pd.read_csv(pred_path, index_col=0)
    
    # make sure that format is correct
    # assert (preds.columns == holdout_labels.columns).all()
    # assert (preds.index == holdout_labels.index).all()
    
    return _multi_multi_log_loss(preds.values, holdout_labels.values)