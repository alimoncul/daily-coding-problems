'''
Grading Students: https://www.hackerrank.com/challenges/grading/problem
'''
#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    for j in range(len(grades)):
        if(grades[j]<=37):
            continue
        else:
            if(grades[j]%5==0):
                continue
            else:
                for i in range(1,3):
                    rounded = grades[j] + i
                    if(rounded%5==0):
                        grades[j] = rounded
    return grades


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
