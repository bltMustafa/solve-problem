"""
Separate Odd and Even Numbers

This program takes a list of integers and splits them into two lists:
- odd numbers
- even numbers

Example:
Input: [1, 2, 3, 4, 5, 6, 7]
Output: {"odd": [1, 3, 5, 7], "even": [2, 4, 6]}
"""

# Solution 1:
input_list = [1, 2, 3, 4, 5, 6, 7]
odd_numbers = []
even_numbers = []

for num in input_list:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

result = {"odd": odd_numbers, "even": even_numbers}
print(f"Solution 1: {result}")


# Solution 2:
result_2 = {
    "odd": [num for num in input_list if num % 2 != 0],
    "even": [num for num in input_list if num % 2 == 0],
}
print(f"Solution 2: {result_2}")


# Solution 3:
result_3 = {"odd": [], "even": []}
for num in input_list:
    if num % 2 == 0:
        result_3["even"].append(num)
    else:
        result_3["odd"].append(num)
print(f"Solution 3: {result_3}")


# Solution 4:
result_4 = {"odd": [], "even": []}
for num in input_list:
    result_4[("even" if num % 2 == 0 else "odd")].append(num)
print(f"Solution 4: {result_4}")

