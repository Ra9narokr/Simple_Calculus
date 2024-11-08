import unittest
from integration import integrate_average

class TestIntegration(unittest.TestCase):
    
    def test_constant_function(self):
        f = 5
        result = integrate_average(f, 0, 10)
        expected = 5
        self.assertAlmostEqual(result, expected, places=5)

    def test_polynomial_function(self):
        f = lambda x: x**2 + x + 1
        result = integrate_average(f, 0, 1)
        expected = (1/4 + 1/2 + 1)
        self.assertAlmostEqual(result, expected, places=5)

if __name__ == "__main__":
    unittest.main()
