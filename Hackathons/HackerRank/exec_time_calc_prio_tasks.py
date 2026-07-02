#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalExecutionTime' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY logs
#

def getTotalExecutionTime(n, logs):
    # Write your code here
    execution_times = [0] * n
    stack = []
    
    for i in range(len(logs)):
        log = logs[i].split(":")
        function_id, action, timestamp = int(log[0]), log[1], int(log[2])
        
        if action == "start":
            if stack:
                last_function_id, last_timestamp = stack[-1]
                execution_times[last_function_id] += timestamp - last_timestamp
            stack.append((function_id, timestamp))
        else:
            last_function_id, last_timestamp = stack.pop()
            execution_times[last_function_id] += timestamp - last_timestamp + 1
            if stack:
                stack[-1] = (stack[-1][0],  timestamp + 1)
              
    return execution_times
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    result = getTotalExecutionTime(n, logs)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
