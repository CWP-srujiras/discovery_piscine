#!/usr/bin/env py
import sys
try:
    num1 = int(input("Give me the first number: ").strip())
    num2 = int(input("Give me the second number: ").strip())
    print("Thank you!")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} / {num2} = {num1 // num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
except:
    pass
