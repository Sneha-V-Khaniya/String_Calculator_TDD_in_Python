import re
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
