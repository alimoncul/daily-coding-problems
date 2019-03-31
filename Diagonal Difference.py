'''
Diagonal Difference: https://www.hackerrank.com/challenges/diagonal-difference/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    leftToRightSum = 0
    rightToLeftSum = 0
    for i in range(len(arr)):
        leftToRightSum += arr[i][i]
    for j in range(len(arr)):
        rightToLeftSum += arr[j][len(arr)-j-1]
    return abs(leftToRightSum-rightToLeftSum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
