import unittest
import re
from calculator import add, NegativeNumberException
class Test(unittest.TestCase):
     
    def test_add_return_sum(self):
        self.assertEqual(add(), 0)
        self.assertEqual(add(""), 0)
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("234"), 234)
        self.assertEqual(add("1,3"), 4)
        self.assertEqual(add("2, 4"), 6)
        self.assertEqual(add("1,2,3"), 6)
        self.assertEqual(add("1, 2, 3, 4, 5"), 15)
        self.assertEqual(add("1\n2"), 3)
        self.assertEqual(add("1,2\n3"), 6)
        self.assertEqual(add("1\n2,3, 4\n 5"), 15)
        self.assertEqual(add("//;\n1;2"), 3)
        self.assertEqual(add("//@\n1@2@3@4@5"), 15)
    
    def test_sum_negative_numbers_raise_exception(self):
        with self.assertRaises(NegativeNumberException) as negative_num_error:
            add("-1")
        self.assertEqual(negative_num_error.exception.args[0], "negative numbers are not allowed -1")
        
        with self.assertRaises(NegativeNumberException) as negative_num_error:
            add("-1,-2,-3,4")
        self.assertEqual(negative_num_error.exception.args[0], "negative numbers are not allowed -1 -2 -3")
        
if __name__ == '__main__':
    unittest.main()
