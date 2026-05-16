#!/usr/bin/env python3
"""
Python script to check if letter 'A' or 'a' is in a list
"""

# Create a list with various items
my_list = ['apple', 'B', 'cat', 'A', 'dog', 'a', 'elephant', 'F']

print("Original list:", my_list)
print()

# Method 1: Using 'in' operator with a loop to check for 'A' or 'a'
if 'A' in my_list or 'a' in my_list:
    print("Method 1: Letter 'A' or 'a' found in the list!")
else:
    print("Method 1: Letter 'A' or 'a' NOT found in the list.")

print()

# Method 2: Using any() with a list comprehension
if any(item.lower() == 'a' for item in my_list if isinstance(item, str)):
    print("Method 2: Letter 'A' or 'a' found in the list!")
else:
    print("Method 2: Letter 'A' or 'a' NOT found in the list.")

print()

# Method 3: Counting occurrences
count = my_list.count('A') + my_list.count('a')
print(f"Method 3: Letter 'A' or 'a' appears {count} time(s) in the list.")

print()

# Method 4: Finding the position/index
positions = []
for i, item in enumerate(my_list):
    if item == 'A' or item == 'a':
        positions.append(i)

if positions:
    print(f"Method 4: Letter 'A' or 'a' found at index/indices: {positions}")
else:
    print("Method 4: Letter 'A' or 'a' NOT found in the list.")
