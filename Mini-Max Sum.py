'''
Mini-Max Sum: https://www.hackerrank.com/challenges/mini-max-sum/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    minimum = 0
    maximum = 0
    for i in range(len(arr)-1):
        minimum += arr[i]
        maximum += arr[i+1]
    print(minimum,maximum)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
