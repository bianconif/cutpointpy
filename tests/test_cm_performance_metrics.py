import numpy as np
import unittest

from cutpointpy.utils import cm_performance_metrics

class TestCmPerformanceMetrics(unittest.TestCase):

    def test_one(self):
        cm = np.array([[2, 4, 1, 6], [3, 0, 1, 4]])
        
        true_metrics = np.zeros(shape=(cm.shape[0], 3))
        true_metrics[:, 0] = [8 / 13, 7 / 8]
        true_metrics[:, 1] = [2 / 6, 3 / 3]
        true_metrics[:, 2] = [6 / 7, 4 / 5]
        
        estimated_metrics = cm_performance_metrics(cm)
        for idx, metric in enumerate(estimated_metrics):
            np.testing.assert_array_equal(
                actual=metric,
                desired=np.expand_dims(true_metrics[:, idx], axis=-1),
                err_msg=f'Test one failed on metric {idx}'
            )
        
if __name__ == '__main__':
    unittest.main()