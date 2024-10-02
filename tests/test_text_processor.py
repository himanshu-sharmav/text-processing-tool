import unittest
from src.text_processor import count_words, count_chars, count_lines, find_word, replace_word
import os

class TestTextProcessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create a sample text file for testing purposes."""
        cls.test_file = 'tests/test_file.txt'
        with open(cls.test_file, 'w') as f:
            f.write("Hello world!\nThis is a test file.\nLet's test word count, character count, and line count.\n")

    @classmethod
    def tearDownClass(cls):
        """Clean up the test file after all tests are done."""
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def test_count_words(self):
        """Test word counting functionality."""
        result = count_words(self.test_file)
        self.assertEqual(result, 16)  


    def test_count_chars(self):
        """Test character counting functionality."""
        result = count_chars(self.test_file)
        self.assertEqual(result, 90)

    def test_count_lines(self):
        """Test line counting functionality."""
        result = count_lines(self.test_file)
        self.assertEqual(result, 3)

    def test_find_word(self):
        """Test word search functionality."""
        result = find_word(self.test_file, 'test')
        self.assertEqual(result, 2)

    def test_replace_word(self):
        """Test word replacement functionality."""
        output_file = 'tests/updated_test_file.txt' 
        new_file = replace_word(self.test_file, 'test', 'exam', output_file) 
        with open(new_file, 'r') as f:
            content = f.read()

        self.assertIn('exam', content)
        self.assertNotIn('test', content)
        # Clean up the replaced file
        if os.path.exists(new_file):
            os.remove(new_file)



if __name__ == '__main__':
    unittest.main()
