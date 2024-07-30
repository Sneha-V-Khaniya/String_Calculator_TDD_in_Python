import unittest

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(), 0)
        self.assertEqual(add(""), 0)
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("234"), 234)
        self.assertEqual(add("1,3"), 4)
        

if __name__ == '__main__':
    unittest.main()

def add(numbers = 0):
    if numbers == 0 or numbers == "":
        return 0
    
    if numbers.isdigit():
        return int(numbers)
    else:
        nums = numbers.split(",")
        _sum = 0
        for i in nums:
            _sum += int(i)
        return _sum
        