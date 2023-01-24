#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            x =arr[i+1];
            while arr[i]>x and i >= 0:
                arr[i+1] = arr[i];
                i -= 1
                print(*arr)
            arr[i+1] = x
            print(*arr)
 
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
