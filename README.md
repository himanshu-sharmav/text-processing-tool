### `README.md`
# Text Processing Tool

A Python-based command-line tool that performs various text file operations such as word count, character count, line count, word search, and word replacement.

## Features
- **Word Count**: Count the total number of words in a text file.
- **Character Count**: Count the total number of characters in a text file.
- **Line Count**: Count the number of lines in a text file.
- **Find Word**: Search for a specific word and display its frequency.
- **Replace Word**: Replace a word with another in the text file and save the modified file.

## Installation

### Clone the Repository
First, clone the repository to your local machine:

```bash
git clone <repository_url>
```

### Navigate to the Project Directory
Change into the project directory:

```bash
cd text-processing-tool
```

### Install Dependencies
Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Running the Tool

To run the tool, use the following syntax:

```bash
python text_processor.py -f <file_path> [options]
```

### Command-Line Options
- `-f, --file`: Specify the input text file (required).
- `-wc, --word-count`: Display the total word count.
- `-cc, --char-count`: Display the total character count.
- `-lc, --line-count`: Display the total line count.
- `-find, --find`: Search for a specific word in the text file.
- `-r, --replace`: Replace a word with another word in the text file. Example: `-r old_word new_word`.

### Example Usage

```bash
python text_processor.py -f sample.txt -wc -cc -find "example" -r "old" "new"
```

Expected output:
```text
Word Count: 1200
Character Count: 7200
The word "example" occurs 5 times.
"old" was replaced with "new" and saved to updated_sample.txt
```

## Testing

To run the test suite, navigate to the project directory and run:

```bash
python -m unittest discover tests
```

## Documentation

The project is documented using Sphinx. To build the HTML documentation:

1. Navigate to the `docs` directory:

   ```bash
   cd docs
   ```

2. Build the HTML documentation:

   ```bash
   make html
   ```

3. The generated HTML files can be found in the `_build/html` directory. Open `index.html` in your browser to view the documentation.

## Contributing

Feel free to open an issue or submit a pull request if you'd like to contribute!

## License

This project is licensed under the MIT License.
```

### Key Sections:
- **Installation**: Step-by-step guide to set up the project.
- **Usage**: Shows how to use the command-line options.
- **Testing**: Instructions for running the test suite.
- **Documentation**: Explains how to generate the HTML documentation using Sphinx.
- **Contributing & License**: Encourage contributions and mention the license type.

Feel free to customize this `README.md` as needed. Let me know if you'd like further improvements!