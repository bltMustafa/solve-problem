"""
Check if a Word Is a Palindrome

This program checks whether a given word reads the same
forward and backward. If it does, the word is considered
a palindrome.

Examples:
Input: "kayak" → Output: True
Input: "araba" → Output: False
"""

input_word = "kayak"


# Solution 1:
is_palindrome = input_word == input_word[::-1]
print(f"Solution 1: {is_palindrome}")


# Solution 2:
is_palindrome_2 = input_word == input_word[::-1]
print(f"Solution 2: {is_palindrome_2}")


# Solution 3:
is_palindrome_3 = True
for i in range(len(input_word) // 2):
    if input_word[i] != input_word[len(input_word) - i - 1]:
        is_palindrome_3 = False
        break
print(f"Solution 3: {is_palindrome_3}")
