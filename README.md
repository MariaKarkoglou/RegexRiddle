# RegexRiddle

<u>Overview</u>
This Python project is a crossword solver that utilizes regular expressions to find and fill in words on a crossword grid. The solver employs various libraries to achieve its functionality, including:

argparse: Used for parsing command-line arguments.
string: Provides string-related operations.
re (regular expression): A module for working with regular expressions.
sre_yield: Enables the generation of strings based on regular expressions.
csv: Facilitates reading and writing CSV files.

<u>Regular Expression Logic</u>

Regular expressions are a sequence of characters that describe patterns within strings. In the context of this crossword solver, we use regular expressions to describe strings where the exact content might not be known, but a certain pattern is recognizable.

With regular expressions, we use characters from the alphabet and some special characters to describe the patterns we're interested in. Here are some key elements:
The special character * indicates that the preceding unit can appear zero or more times. So, the regular expression ca*t describes the strings ct, cat, caat, and so on.
The special character + means that the preceding unit can appear one or more times. Thus, the regular expression ca+t describes the strings cat, caat, caaat, and so forth.
The special character ? signifies that the preceding unit can appear zero or one time. Consequently, the regular expression ca?t describes the strings ct and cat.

These regular expressions allow us to match and find variations of words, accommodating different spellings or formats within the crossword puzzle and wordlist.

<u>Usage</u>
The program is called as follows (where python is the appropriate command for your system):
python re_crossword.py crossword_file regular_expressions_file

The significance of the parameters is as follows:
crossword_file: The file describing the crossword structure, it can have any name.
The crossword_file should be in CSV (Comma Separated Values) format. Each line consists of fields separated by commas:
Word in the crossword.
String representing the contents of the word. Unknown characters are represented by dots (.).
One or more pairs of numbers. The first number in each pair indicates a word intersecting with the current word. The second number indicates the position of the intersection character in the current word.

regular_expressions_file: The file containing the regular expressions to be used. The same observation about the name applies here as well.

The program's output will be a series of lines in the format:
X regex word
Where X is the word number, regex is the matching regular expression, and word is the resulting word from the expansion of the regular expression. The lines should be sorted in ascending order based on the word.

<u>Test Files</u>
To help users test the algorithm, two sample files are included in the repository:

Crossword Puzzle File: films.csv

Regular Expression File: films.txt
