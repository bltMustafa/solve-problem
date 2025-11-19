"""
Reverse a String

This program takes a string as input and returns a new string
that is the reversed version of the original.

Example:
Input: "mustafa"
Output: "afatsum"
"""

# Solution 1:
input_string = "MUSTAFA"
reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string

print(f"Solution 1: {reversed_string}")


# Solution 2:
reversed_string_2 = input_string[::-1]
print(f"Solution 2: {reversed_string_2}")


# Solution 3:   using reverse() method
reversed_string_3 = list(input_string)
reversed_string_3.reverse()
print(f"Solution 3: {''.join(reversed_string_3)}")


#Solution 4:   using recursion
def reverse_string(input_string):
    if len(input_string) == 0:
        return input_string
    else:
        return reverse_string(input_string[1:]) + input_string[0]
print(f"Solution 4: {reverse_string(input_string)}")