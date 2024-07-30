import re

class NegativeNumberException(Exception):
    def __init__(self, negative_numbers):
        self.negative_numbers = negative_numbers
        super().__init__(f"negative numbers are not allowed {negative_numbers}")

def check_for_negative_numbers(numbers):
    negative_pattern = r'-\d+'
    negative_nums = re.findall(negative_pattern, numbers)
    
    if len(negative_nums) != 0:
        raise NegativeNumberException(negative_nums)

def add(numbers = 0):
    try:
        if numbers == 0 or numbers == "":
            return 0
        
        if numbers.isdigit():
            return int(numbers)
        
        check_for_negative_numbers(numbers)
        
        if numbers[0:2] != "//":
            nums = []
            list_items = re.split(r'[,\n]', numbers)
            for item in list_items:
                nums.append(item)
            
        else:
            delimiter = numbers[2]
            numbers = numbers[4:]
            nums = re.split(delimiter, numbers)
        
        _sum = 0
        for i in nums:
            _sum += int(i)
        return _sum
    except NegativeNumberException as e:
        print(f"negative numbers are not allowed {e.negative_numbers}")
        raise
add("-1")