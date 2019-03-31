'''
Time Conversion: https://www.hackerrank.com/challenges/time-conversion/problem
'''
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    timeGate = s[-2:]
    time = s[:2]
    if(timeGate=="PM"):
        if(time!="12"):
            hour = int(s[:2]) + 12
            return(str(hour)+s[2:-2])
        else:
            return s[:-2]
    elif(timeGate=="AM"):
        if(time=="12"):
            print("00"+s[2:-2])
            return("00"+s[2:-2])
        return s[:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
