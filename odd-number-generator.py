# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 08:345:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("Random Odd Number Generator")
print(Fore.GREEN+font)

import random

# Function to generate 6 random odd numbers
def generate_odd_numbers():
    odd_numbers = []
    while len(odd_numbers) < 6:
        num = random.randint(1, 100)  # Generate a random number between 1 and 100
        if num % 2 != 0:  # Check if the number is odd
            odd_numbers.append(num)
    return odd_numbers

# Generate and print the 6 odd numbers
odd_numbers = generate_odd_numbers()
print("Generated 6 random odd numbers:", odd_numbers)
