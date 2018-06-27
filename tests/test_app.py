import unittest

from SamplePythonUnitTestProject.app import div, fact, flatten, gcd

class TestSampleFunctions(unittest.TestCase):

    def test_div(self):
        self.assertEqual(div(20, 40), [21, 28], "Your div function does not seem to be working.")

    def test_fact(self):
        self.assertEqual(fact(5), 120, "Your fact function does not seem to be working.")

    def test_flatten(self):
        self.assertEqual(flatten([[1, 2], 3, [4], 5, [6, 7], [[],[]]]), [1, 2, 3, 4, 5, 6, 7], "Your flatten function does not seem to be working.")

    def test_gcd(self):
        self.assertEqual(gcd([43023, 393, 8373, 445, 66,5, 900, 32323, 452534, 59945]), 1, "Your gcd function does not seem to be working.")

if __name__ == '__main__':
    unittest.main()