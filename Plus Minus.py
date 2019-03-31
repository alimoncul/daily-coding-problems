'''
Plus Minus: https://www.hackerrank.com/challenges/plus-minus/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    numberRatios = [0,0,0]
    for i in range(len(arr)):
        if(arr[i]>0):
            numberRatios[2] += 1
        elif(arr[i]<0):
            numberRatios[0] += 1
        elif(arr[i]==0):
            numberRatios[1] += 1
    for j in range(len(numberRatios)):
        numberRatios[j] = numberRatios[j] / len(arr)
    print(numberRatios[2])
    print(numberRatios[0])
    print(numberRatios[1])
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
