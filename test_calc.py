import unittest

from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        pass

    def test_of_test(self):
        self.assertTrue(True)

    def test_add(self):
        result = Calc.add(2, 2)
        self.assertEqual(result, 4)

    def test_sub(self):
        result = Calc.sub(10, 5)
        self.assertEqual(result, 5)

    def test_sub_negative(self):
        result = Calc.sub(5, 10)
        self.assertEqual(result, -5)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()