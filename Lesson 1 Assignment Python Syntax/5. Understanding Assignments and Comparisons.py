# Objective:
# The aim of this assignment is to get a grasp on how assignment operators work and how values can be compared using comparison operators.

# Task 1: Value Swapping
# Swap the values of two given numbers using assignment operators (=) and then compare them to ensure they have been swapped.

value_one, value_two=10,20

print("Before Swap")
print("value one=", value_one)
print("value two=", value_two)

value_one,value_two= value_two, value_one

print("After Swap")
print("value one=", value_one)
print("value two=", value_two)