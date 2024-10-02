import argparse
from pathlib import Path

def count_words(file_path: str) -> int:
    """Count the total number of words in the specified text file.

    Parameters:
        file_path (str): The path to the text file.

    Returns:
        int: The total number of words in the file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    with open(file_path, 'r') as f:
        text = f.read()
        words = text.split()
        return len(words)  


def count_chars(file_path: str) -> int:
    """
    Count the total number of characters in the file.

    :param file_path: The path to the file to be processed.
    :return: The total number of characters in the file.
    :raises FileNotFoundError: If the file does not exist.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    return len(content)

def count_lines(file_path: str) -> int:
    """
    Count the total number of lines in the file.

    :param file_path: The path to the file to be processed.
    :return: The total number of lines in the file.
    :raises FileNotFoundError: If the file does not exist.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return len(lines)

def find_word(file_path: str, word: str) -> int:
    """
    Find the frequency of a specific word in the file.

    :param file_path: The path to the file to be processed.
    :param word: The word to search for.
    :return: The number of occurrences of the word in the file.
    :raises FileNotFoundError: If the file does not exist.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    return content.lower().split().count(word.lower())

def replace_word(file_path: str, old_word: str, new_word: str, output_file: str) -> str:
    """Replace a specific word in the text file and save the modified content to a new file.

    Parameters:
        file_path (str): The path to the input text file.
        old_word (str): The word to be replaced.
        new_word (str): The word to replace with.
        output_file (str): The path where the modified file will be saved.

    Returns:
        str: The path to the new output file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    with open(file_path, 'r') as f:
        content = f.read()
    
    new_content = content.replace(old_word, new_word)
    
    with open(output_file, 'w') as f:
        f.write(new_content)
    
    return output_file  # Ensure this returns the output file name


def main():
    """
    Main function to handle command-line arguments and call respective functions
    to process the text file.
    """
    parser = argparse.ArgumentParser(description="Process a text file with various operations.")
    parser.add_argument('-f', '--file', required=True, help="Path to the input text file.")
    parser.add_argument('-wc', '--word-count', action='store_true', help="Count total words.")
    parser.add_argument('-cc', '--char-count', action='store_true', help="Count total characters.")
    parser.add_argument('-lc', '--line-count', action='store_true', help="Count total lines.")
    parser.add_argument('-find', '--find', type=str, help="Find a word in the text file.")
    parser.add_argument('-r', '--replace', nargs=2, metavar=('old_word', 'new_word'), help="Replace a word with a new one.")

    args = parser.parse_args()

    if not Path(args.file).exists():
        print(f"Error: The file {args.file} was not found.")
        return

    if args.word_count:
        print(f"Word Count: {count_words(args.file)}")

    if args.char_count:
        print(f"Character Count: {count_chars(args.file)}")

    if args.line_count:
        print(f"Line Count: {count_lines(args.file)}")

    if args.find:
        freq = find_word(args.file, args.find)
        print(f'The word "{args.find}" occurs {freq} times.')

    if args.replace:
        old_word, new_word = args.replace
        output_file = f"updated_{Path(args.file).stem}.txt"
        replace_word(args.file, old_word, new_word, output_file)

if __name__ == '__main__':
    main()
