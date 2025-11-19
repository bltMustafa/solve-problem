"""
Find the Largest and Smallest Numbers in a List

This program takes a list of integers from the user (or a predefined list)
and determines the maximum and minimum values within the list.

Example:
Input: [3, 15, 7, 1, 22]
Output: max = 22, min = 1
"""

# Solution 1:

input_list = [3, 15, 7, 1, 22]

max_number = max(input_list)
min_number = min(input_list)
print(f"Solution 1: max = {max_number}, min = {min_number}")


# Solution 2:
print(f"Solution 2: max = {max(input_list)}, min = {min(input_list)}")
