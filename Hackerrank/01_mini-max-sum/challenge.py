import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    first = sum(arr[0:4])
    last  = sum(arr[1:5])
    print(f"{first} {last}")

    # return sum(first[0:4]) + " " + sum(last[0:4])
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
