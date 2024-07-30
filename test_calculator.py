import unittest
import re
class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(), 0)
        self.assertEqual(add(""), 0)
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("234"), 234)
        self.assertEqual(add("1,3"), 4)
        self.assertEqual(add("2, 4"), 6)
        self.assertEqual(add("1,2,3,4,5"), 15)
        self.assertEqual(add("1, 2, 3, 4, 5"), 15)
        self.assertEqual(add("1\n2"), 3)
        self.assertEqual(add("1,2\n3"), 6)
        self.assertEqual(add("1\n2,3, 4\n 5"), 15)
        

if __name__ == '__main__':
    unittest.main()

def add(numbers = 0):
    if numbers == 0 or numbers == "":
        return 0
    
    if numbers.isdigit():
        return int(numbers)
    else:
        nums = re.split(r'[,\n]', numbers)
        _sum = 0
        for i in nums:
            _sum += int(i)
        return _sum
    
    