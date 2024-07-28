# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:28:09 2024

@author: iharms
"""

import re
import os

def split_file_by_pattern(input_file):
    # Read the entire input file with UTF-8 encoding
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the regex pattern
    pattern = r'(# @\w+_BEG_\w+)'

    # Find all matches of the pattern with their positions
    matches = [(match.group(0), match.start(), match.end()) for match in re.finditer(pattern, content)]

    # Create directory to store the split files (if it doesn't exist)
    output_dir = os.path.splitext(input_file)[0] + "_split"
    os.makedirs(output_dir, exist_ok=True)

    # Split content based on the pattern and write segments to separate files
    for i, match in enumerate(matches):
        # Determine start and end positions for the current segment
        start = match[1]
        if i + 1 < len(matches):
            end = matches[i + 1][1]
        else:
            end = len(content)

        # Extract segment content including the pattern
        segment = content[start:end].strip()

        # Generate file names
        # number_pattern.txt
        file_name = f"{i+1:04d}_{match[0].strip('# @').replace('_BEG_', '_')}.txt"
        output_path = os.path.join(output_dir, file_name)

        # Write segment to files
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(segment)

        print(f'Saved segment {i+1} to {file_name}')

    print(f'Files are saved in directory: {output_dir}')

# Function to check contents of a directory
def check_directory_contents(directory):
    # List all files and directories in the specified directory
    contents = os.listdir(directory)

    # Print the list of contents
    print(f"Contents of directory '{directory}':")
    for item in contents:
        print(item)

# Example usage:
input_file = 'WSACD.txt'  # Replace with your input file name/path
split_file_by_pattern(input_file)

# Check contents of the output directory
output_dir = os.path.splitext(input_file)[0] + "_split"
check_directory_contents(output_dir)
