#!/usr/bin/env py
import sys
if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i <= 10:
        j = 0
        res = []
        while j <= 10:
            res.append(str(i * j))
            j += 1
        print(f"Table de {i}: " + " ".join(res))
        i += 1
