#!/bin/python3
import sys
import math

def factorize_number(num):
    """Finds two factors of num such that num = p * q."""
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            return i, num // i
    return None, None


def getlines():
    """Reads a file line by line and save the data to a list"""
    if len(sys.argv) < 2:
        print("Usage: factors <file>")
        return []

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"No file found: {filename}")
        return []
    return lines


def is_prime(num):
    """Returns true if num is a prime number, false otherwise"""
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return True
    return False