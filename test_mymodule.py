# test the 2 functions defined in mymodule
import unittest
from mymodule import square, double

#create 2 test functions they must always start with test
class TestSquare(unittest.TestCase): 
    def test_square(self):
        self.assertEqual(square(2),4)

class TestDouble(unittest.TestCase):
    def test_double(self):
        self.assertEqual(double(4),8)

if  __name__ == '__main__':
        unittest.main()
    