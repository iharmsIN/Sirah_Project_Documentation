import os
import re

# Define the list of phrases
phrases = [
    "كتاب المبتدأ",
    "كتاب المبعث",
    "كتاب المغازي",
    "كتاب الايام",
    "كتاب السنة الرسول الله",
    "تراجم"
]

# Function to find files containing any of the specified phrases
def find_files_with_phrases(folder_path, phrases):
    files_with_phrases = []

    # List all files in the folder
    files = os.listdir(folder_path)

    # Iterate through each file
    for file in files:
        file_path = os.path.join(folder_path, file)

        # Check if the file is a text file (you can modify the check if needed)
        if file.endswith('.txt'):
            # Read the content of the file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if any of the phrases exist in the content
            for phrase in phrases:
                if phrase in content:
                    files_with_phrases.append(file)
                    break  # No need to check further if one phrase is found

    return files_with_phrases

# Example usage:
def main():
    folder_path = 'WSACD_split'  # Replace with the path to your folder
    
    # Find files containing any of the specified phrases
    files_with_phrases = find_files_with_phrases(folder_path, phrases)

    # Print the list of files found
    if files_with_phrases:
        print("Files containing any of the specified phrases:")
        for file in files_with_phrases:
            print(file)
    else:
        print("No files found containing any of the specified phrases.")

if __name__ == "__main__":
    main()
