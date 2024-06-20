#!/bin/python3
import sys

lines = []
try:
    with open(sys.argv[1]) as file:
        lines = file.readlines()
except (FileNotFoundError, IndexError) as e:
    print("No file found")
    # sys.exit(1)

for line in lines:
    num = int(line)

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            print(f"{num}={num//i}*{i}")
            break