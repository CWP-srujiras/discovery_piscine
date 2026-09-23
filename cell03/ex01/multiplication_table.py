#!/usr/bin/env py
import sys
try:
    print("Enter a number")
    num = int(input().strip())
    i = 0
    while i <= 9:
        print(f"{i} x {num} = {i * num}")
        i += 1
except:
    pass
