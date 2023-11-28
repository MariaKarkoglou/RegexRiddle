# RegexRiddle

## Overview

This Python project, RegexRiddle, is a crossword solver designed to utilize the power of regular expressions for finding and filling in words on a crossword grid. The solver makes use of several essential libraries to achieve its functionality:

- `argparse`: Used for parsing command-line arguments.
- `string`: Provides string-related operations.
- `re` (regular expression): A module for working with regular expressions.
- `sre_yield`: Enables the generation of strings based on regular expressions.
- `csv`: Facilitates reading and writing CSV files.

## Regular Expression Logic

Regular expressions are sequences of characters that describe patterns within strings. In the context of this crossword solver, regular expressions are employed to describe strings where the exact content might not be known, but a certain pattern is recognizable.

### Key Elements:

- The special character `*` indicates that the preceding unit can appear zero or more times. For example, the regular expression `ca*t` describes the strings `ct`, `cat`, `caat`, and so on.
  
- The special character `+` means that the preceding unit can appear one or more times. Thus, the regular expression `ca+t` describes the strings `cat`, `caat`, `caaat`, and so forth.
  
- The special character `?` signifies that the preceding unit can appear zero or one time. Consequently, the regular expression `ca?t` describes the strings `ct` and `cat`.

These regular expressions enable the matching and finding of variations of words, accommodating different spellings or formats within the crossword puzzle and wordlist.

## Usage

The program is called as follows (where `python` is the appropriate command for your system):

python re_crossword.py crossword_file regular_expressions_file

## Parameters:

crossword_file: The file describing the crossword structure, which can have any name. The crossword_file should be in CSV (Comma Separated Values) format. Each line consists of fields separated by commas:

- Word in the crossword.
- String representing the contents of the word. Unknown characters are represented by dots (.).
- One or more pairs of numbers. The first number in each pair indicates a word intersecting with the current word. The second number indicates the position of the intersection character in the current word.

regular_expressions_file: The file containing the regular expressions to be used. The same observation about the name applies here as well. The regular_expressions file should be in txt format.

## Output Format:
The program's output will be a series of lines in the format:

X regex word

Where X is the word number, regex is the matching regular expression, and word is the resulting word from the expansion of the regular expression. The lines should be sorted in ascending order based on the word.

## Test Files
To help users test the algorithm, two sample files are included in the repository:

- Crossword Puzzle File: films.csv
- Regular Expression File: films.txt
