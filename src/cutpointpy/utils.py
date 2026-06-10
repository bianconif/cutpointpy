import numpy as np

def check_same_length(*args):
    """
    Check if iterables have the same length.
    
    Parameters
    ----------
    args :
        The iterables to be compared for equal length.
        
    Returns
    -------
    same_length : bool
        True if all `àrgs` have the same length, False otherwise.
    """
    if not (len(args) > 1):
        raise ValueError('At least two iterables should be given.')

    first_len = len(args[0])
    same_length = all(len(arg) == first_len for arg in args)
    
    return same_length

def cm(predicted, target):
    """
    Confusion matrix for a binary outcome.
    
    Parameters
    ----------
    predicted : ndarray of bool (n_tests, n_samples)
        The predicted labels.
    target : ndarray of bool (n_tests, n_samples)
        The target labels (ground truth).
                       
    Returns
    -------
    cm : ndarray of bool (n_tests, 4)
        The confusion matrices. Each row represents one matrix; columns
        0 to 3 respectively report the number of true positives, false
        negatives, false positives and true negatives.
        
    Notes
    -----
    Vectorised function - computes n_tests confusion matrices at once.
    Convention for labels: True denotes the positive class.
    """
    
    if not (predicted.shape == target.shape):
        raise ValueError('Predicted and target values must have the'
                         'same shape')

    cm = np.zeros(shape=(predicted.shape[0], 4), dtype=np.uint)

    cm[:, 0] = np.sum(np.equal(predicted, True)
                      & np.equal(target, True), axis=1)
    cm[:, 1] = np.sum(np.equal(predicted, False)
                      & np.equal(target, True), axis=1)
    cm[:, 2] = np.sum(np.equal(predicted, True)
                      & np.equal(target, False), axis=1)
    cm[:, 3] = np.sum(np.equal(predicted, False)
                      & np.equal(target, False), axis=1)
    
    return cm

def cm_performance_metrics(cm):
    """
    Performance metrics from the confusion matrix.
    
    Parameters
    ----------
    cm : ndarray of bool (n_matrices, 4)
        The confusion matrices. Each row represents one matrix; columns
        0 to 3 respectively report the number of true positives, false
        negatives, false positives and true negatives.
        
    Returns
    -------
    acc : ndarray of float (n_matrices, 1)
        Accuracy.
    se : ndarray of float (n_matrices, 1)
        Sensitivity.
    sp : ndarray of float (n_matrices, 1)
        Specificity.
        
    Notes
    -----
    Returned values are for each confusion matrix. Accuracy, sensitivity
    and specificity range between 0.0 and 1.0.
    """
    
    acc = (cm[:, 0] + cm[:, 3]) / np.sum(cm, axis=1)
    se = cm[:, 0] / (cm[:, 0] + cm[:, 1])
    sn = cm[:, 3] / (cm[:, 3] + cm[:, 2])
    
    retval = list()
    for item in [acc, se, sn]:
        retval.append(np.array(item, ndmin=2).T)
    
    return retval