"""
Lowest common multiple of two numbers
"""

def lcm(num1, num2):
    temp_num = num1
    while (temp_num % num2) != 0:
        temp_num += num1
    return temp_num
