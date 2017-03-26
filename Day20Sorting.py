#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

totalSwap = 0
if n>=2:
    for ind in range(n-1):
        numSwap = 0
        for j in range(n-1-ind):
            if a[j]>a[j+1]:
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
                numSwap += 1
        if numSwap == 0:
            break
        totalSwap += numSwap
print("Array is sorted in "+str(totalSwap)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[n-1]))