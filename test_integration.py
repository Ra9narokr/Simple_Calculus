import unittest
from integration import integrate_average

class TestIntegration(unittest.TestCase):
    
    def test_constant_function(self):
        f = lambda x: 5
        result = integrate_average(f, 0, 10)
        expected = 5
        self.assertAlmostEqual(result, expected, places=5)

    def test_polynomial_function(self):
        f = lambda x: x**2 + x + 1
        result = integrate_average(f, 0, 1)
        fault_ans = 1.75
        correct_ans = 1.8333333333333335
        self.assertAlmostEqual(result, correct_ans, places=5)

if __name__ == "__main__":
    unittest.main()
