import os
import re

# Function to extract numeric prefixes from filenames
def extract_prefix(filename):
    match = re.match(r'^(\d{4})_(\d{4})_', filename)
    if match:
        return (int(match.group(1)), int(match.group(2)))
    else:
        return (0, 0)

# Folder containing the text files
folder_path = 'WAIYA_split_Copy'

# Output combined file name
output_file = 'WAIYA_combined_files.txt'

# List to hold all file contents
file_contents = []

# Iterate over all files in the folder
for filename in sorted(os.listdir(folder_path), key=extract_prefix):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents.append(file.read())
            file_contents.append('\n\n')

# Write all contents to the output combined file
with open(os.path.join(folder_path, output_file), 'w', encoding='utf-8') as combined_file:
    combined_file.write(''.join(file_contents))

print(f'Combined files saved to {os.path.join(folder_path, output_file)}')
