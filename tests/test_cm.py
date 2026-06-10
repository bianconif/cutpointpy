import numpy as np
import unittest

from cutpointpy.utils import cm

class TestCm(unittest.TestCase):

    def test_one(self):
        predicted = np.array([[False, False, True],
                              [False, True, False]])

        target = np.array([[False, False, False],
                           [True, True, False]])

        true_cm = np.array([[0, 0, 1, 2], [1, 1, 0, 1]])
        computed_cm = cm(predicted, target)
        np.testing.assert_array_equal(
            actual=computed_cm, desired=true_cm, err_msg='Test one failed.'
        )

    def test_two(self):
        predicted = np.array([[False, False, True, True],
                              [True, True, False, True],
                              [False, True, False, True]])
        
        target = np.array([[False, True, True, True],
                           [False, True, True, False],
                           [False, True, False, True]])
        
        true_cm = np.array(
            [[2, 1, 0, 1], [1, 1, 2, 0], [2, 0, 0, 2]])
        computed_cm = cm(predicted, target)
        np.testing.assert_array_equal(
            actual=computed_cm, desired=true_cm, err_msg='Test two failed.'
        )
        
if __name__ == '__main__':
    unittest.main()        