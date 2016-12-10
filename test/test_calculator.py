import unittest
from app.calculator import Calculator

class TddPythonExample(unittest.TestCase):

    def test_calculator_add_method_returns_correct_result(self):
        cal = Calculator()
        result = cal.add(2, 2)
        self.assertEqual(4, result)

if __name__ == '__main__':
    unittest.main()
