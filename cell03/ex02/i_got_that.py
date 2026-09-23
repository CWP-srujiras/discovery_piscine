#!/usr/bin/env py
import sys
try:
    user_input = input("What you gotta say? : ")
    while True:
        if user_input == "STOP":
            break
        user_input = input("I got that! Anything else? : ")
except:
    pass
