"""
Credits
-------
Calculation of target AUCs based on: 
https://www.emathhelp.net/calculators/calculus-2/
trapezoidal-rule-calculator-for-a-table 
"""

import numpy as np
import unittest

from cutpointpy.utils import auc

class TestCm(unittest.TestCase):

    def test_one(self):
        se = np.array([[0, 1/2, 3/4, 1]])
        sp = np.array([[1, 3/4, 1/4, 0]])

        target_aucs = np.array([[19/32]])
        computed_aucs = auc(se, sp)
        
        np.testing.assert_allclose(
            actual=target_aucs,
            desired=computed_aucs,
            err_msg='Test one failed.')
        
    def test_two(self):
        se = np.array([[1/5, 2/5, 2/5, 3/5, 4/5],
                       [0, 3/5, 4/5, 4/5, 3/5]])
        sp = np.array([[1, 4/5, 3/5, 1/5, 0],
                       [1, 4/5, 3/5, 2/5, 0]])

        target_aucs = np.array([[12/25],
                                [16/25]])
        computed_aucs = auc(se, sp)
        
        np.testing.assert_allclose(
            actual=target_aucs,
            desired=computed_aucs,
            err_msg='Test two failed.')    
        
if __name__ == '__main__':
    unittest.main()