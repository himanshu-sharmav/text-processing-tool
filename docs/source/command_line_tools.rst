Command Line Tools
==================

The command-line tool supports the following arguments:

- ``--file`` or ``-f``: Specify the path to the input file.
- ``--word-count`` or ``-wc``: Display the word count.
- ``--char-count`` or ``-cc``: Display the character count.
- ``--line-count`` or ``-lc``: Display the line count.
- ``--find`` or ``-find``: Find the frequency of a word in the text file.
- ``--replace`` or ``-r``: Replace one word with another.

Example usage:
--------------
.. code-block:: bash

   python text_processor.py -f sample.txt -wc -cc -find "word" -r "old" "new"
