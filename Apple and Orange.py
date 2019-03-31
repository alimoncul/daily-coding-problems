'''
Apple and Orange: https://www.hackerrank.com/challenges/apple-and-orange/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount, orangeCount = 0,0
    for i in range(len(apples)):
        if(apples[i]+a<=t and apples[i]+a>=s):
            appleCount += 1
    for j in range(len(oranges)):
        if(oranges[j]+b<=t and oranges[j]+b>=s):
            orangeCount += 1
    print(appleCount)
    print(orangeCount)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
