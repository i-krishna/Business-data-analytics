# There is a straight line of students of various heights. The students' heights are given in the form of an array, in the order they are standing in the line.
# Consider the region of a student as the length of the largest subarray that includes that student's position,
# and in which that student's height is equal to maximum height among all students present in that subarray. Return the sum of the region of all students.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'calculateTotalRegion' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY heights as parameter.

def calculateTotalRegion(heights):
    n = len(heights)
    left = [-1] * n
    right = [n] * n

    # Monotonic stack for left boundary
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    # Monotonic stack for right boundary
    stack = []
    for i in range(n-1, -1, -1):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    total = 0
    for i in range(n):
        total += right[i] - left[i] - 1

    return total


"""
def calculateTotalRegion(heights):
    n = len(heights)
    if n == 0:
        return 0
    # Arrays to hold index of previous greater (L) and next greater (R)
    L = [-1] * n
    R = [n] * n
    
    stack = []
    # Find previous greater for each index
    for i in range(n):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()
        L[i] = stack[-1] if stack else -1
        stack.append(i)
    
    stack = []
    # Find next greater for each index
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()
        R[i] = stack[-1] if stack else n
        stack.append(i)
    
    total = 0
    # Sum lengths of regions (R[i] - L[i] - 1)
    for i in range(n):
        total += (R[i] - L[i] - 1)
    return total

# Example:
print(calculateTotalRegion([3, 5, 6]))  # Output: 6
"""


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    heights_count = int(input().strip())

    heights = []

    for _ in range(heights_count):
        heights_item = int(input().strip())
        heights.append(heights_item)

    result = calculateTotalRegion(heights)

    fptr.write(str(result) + '\n')

    fptr.close()
