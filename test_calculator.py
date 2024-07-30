import unittest
import re

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


class NegativeNumberException(Exception):
    def __init__(self, negative_num_list):
        self.negative_num_list = negative_num_list
        negative_numbers = ' '.join(self.negative_num_list)
        super().__init__(f"negative numbers are not allowed {negative_numbers}")

def check_for_negative_numbers(input_str):
    negative_num_pattern = r'-\d+'
    negative_num_list = re.findall(negative_num_pattern, input_str)
    
    if len(negative_num_list) != 0:
        raise NegativeNumberException(negative_num_list)

def add(input_str = "0"):
    
    if input_str.isdigit():
        return int(input_str)
    
    if input_str == "":
        return 0
    
    check_for_negative_numbers(input_str)
    
    if input_str[0:2] != "//":
        num_list = re.split(r'[,\n]', input_str)
    else:
        delimiter = input_str[2]
        input_str = input_str[4:]
        num_list = re.split(delimiter, input_str)
    
    _sum = 0
    for num in num_list:
        _sum += int(num)
    return _sum
    
