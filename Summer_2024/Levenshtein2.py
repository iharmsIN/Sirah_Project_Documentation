import os
import re
import csv
import Levenshtein  # Import Levenshtein module
from arabic_reshaper import reshape  # Optional: for better Arabic text display
from bidi.algorithm import get_display  # Optional: for better Arabic text display

# Function to normalize Arabic text (simplified example)
def normalize_arabic_text(text):
    # Example: Remove diacritics
    text = remove_diacritics(text)

    # Example: Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text

# Example of removing diacritics (simplified)
def remove_diacritics(text):
    # Example: Replace diacritics with empty string
    diacritics_pattern = r'[\u064B-\u0652]'  # Arabic diacritics Unicode range
    return re.sub(diacritics_pattern, '', text)

# Function to read and normalize all text files in a folder
def normalize_text_files(folder_path):
    normalized_texts = []
    file_order = []

    # List all files in the folder
    files = os.listdir(folder_path)

    # Sort files based on numeric prefix (first sequence of digits)
    sorted_files = sorted(files, key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else float('inf'))

    # Process each file
    for file in sorted_files:
        file_path = os.path.join(folder_path, file)

        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        # Normalize Arabic text using custom rules
        normalized_text = normalize_arabic_text(text)

        # Store normalized text and file order
        normalized_texts.append(normalized_text)
        file_order.append(file)

    return normalized_texts, file_order

# Function to calculate Levenshtein distance between two texts
def calculate_levenshtein_distance(target_text, reference_text):
    return Levenshtein.distance(target_text, reference_text)

# Function to rank target files based on similarity to training files and output CSV
def rank_target_files_by_similarity(training_texts, training_file_order, target_texts, target_file_order, target_folder, csv_output_file):
    # Initialize a list to store similarity scores
    similarity_scores = []

    # Iterate over each target text
    for target_text in target_texts:
        # Initialize a list to store distances to each training text and their corresponding filenames
        distances_with_training = []

        # Compare target text with each training text
        for training_text in training_texts:
            distance = calculate_levenshtein_distance(target_text, training_text)
            distances_with_training.append((distance, training_text))

        # Find the index of the minimum distance (most similar training text)
        min_distance_index = min(range(len(distances_with_training)), key=lambda i: distances_with_training[i][0])
        min_distance, most_similar_file = distances_with_training[min_distance_index]

        # Determine the rank where the target file should be placed (use +1 because list index starts from 0)
        rank = min_distance_index + 1

        # Rename the target file based on the determined rank
        old_file = target_file_order.pop(0)
        old_file_path = os.path.join(target_folder, old_file)
        new_file_name = f"{rank:04d}_{old_file}"  # Prefix with rank and underscore
        new_file_path = os.path.join(target_folder, new_file_name)
        os.rename(old_file_path, new_file_path)
        print(f'Renamed "{old_file}" to "{new_file_name}"')

        # Clean passage names for CSV output
        passage_name = re.sub(r'^\d+_', '', os.path.splitext(old_file)[0])
        most_similar_passage_name = re.sub(r'^\d+_', '', os.path.splitext(most_similar_file)[0])

        # Collect data for CSV output
        similarity_scores.append({
            'created_file_name': new_file_name,
            'passage_name': passage_name[4:],  # Remove first 4 characters
            'WZATB_passage': most_similar_passage_name[4:],  # Remove first 4 characters
            'levenshtein_distance': min_distance
        })

    # Write CSV file
    headers = ['created_file_name', 'passage_name', 'WZATB_passage', 'levenshtein_distance']
    with open(csv_output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(similarity_scores)

    print(f"Saved CSV file with similarity scores to '{csv_output_file}'")

# Example usage:
def main():
    # Replace with your folder paths
    training_folder = 'WSACD_split'  # Folder containing training files
    target_folder = 'WAIYA_split_Copy'  # Target folder containing files to be organized
    csv_output_file = 'similarity_scores.csv'  # Output CSV file name for similarity scores

    # Normalize texts in training folder
    training_texts, training_file_order = normalize_text_files(training_folder)

    # Normalize texts in target folder and get file order
    target_texts, target_file_order = normalize_text_files(target_folder)

    # Rank target files based on similarity to training files and output CSV
    rank_target_files_by_similarity(training_texts, training_file_order, target_texts, target_file_order, target_folder, csv_output_file)

if __name__ == "__main__":
    main()
