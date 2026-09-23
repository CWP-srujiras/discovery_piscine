#!/usr/bin/env py
import sys
try:
    num = float(input("Give me a number: ").strip())
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except:
    pass
