#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countDuplicate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def countDuplicate(numbers):
    # Use a dictionary to count the occurrences of each number
    count_map = {}
    for num in numbers:
        count_map[num] = count_map.get(num, 0) + 1

    # Count the number of elements that appear more than once
    duplicate_count = sum(1 for count in count_map.values() if count > 1)

    return duplicate_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = countDuplicate(numbers)

    fptr.write(str(result) + '\n')

    fptr.close()
