import os
from collections import Counter

# File Manipulation:
# Create a program that reads a text file and counts the occurrences of each word.
# Display the word frequency in descending order.


file_path = os.path.join(r"C:\Users\VerViz-01\Projects\FileManipulator\LoremIpsum.txt")

if os.path.isfile(file_path):
    try:
        with open(file_path, "r") as file:
            fileOpen = file.read()
            countWords = Counter(fileOpen.split())

            # Print word frequencies in a column-like order
            if 'countWords' in locals():
                print("words\t\tFrequency")
                print("-------------------------")
                for word, count in countWords.most_common():
                    print(f"{word.ljust(15)}{count}")
    except FileNotFoundError as error:
        print(f"FileNotFoundError: {error}")
else:
    print("Error: The specified file does not exist or not readable.")