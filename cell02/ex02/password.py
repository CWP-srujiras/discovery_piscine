#!/usr/bin/env py
import sys
password = "Python is awesome"
try:
    user_input = input().strip()
    if user_input == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
except:
    pass
