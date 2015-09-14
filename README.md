# feckless-guacamole
Author: Jon Collins
Date: 13-Sep-2015
Purpose: Extract all data from website with specified text string, exclude table data

Time spent: Approx 4 hours

OS: Windows Vista or higher (see notes below)

Python Version: 3.4.3

Libraries used: 
  bs4 (Beautiful Soup 4.4.0)
  urllib
  re
  os
  sys

Method:

1. Extract html doc and save to text file.
2. Search html file for text with specified string in text, exclude all tags with table data (tag = 'table') in the parent nodes. 
3. Find text in html doc file and get start and end index.
4. Write text, start index, and end index to second text file.
 
Instructions for running:

From the command line, type:

  python.exe <url> <text>
  
Where <url> is a valid url (string) and <text> is the text string to search for. 

Output location:
  The output files are located at "C:\Practical"

Notes:
Due to time limit, only Windows is supported. To convert to Linux/Unix, simply modify the output directory to a Unix-like     directory.
  
Currently, not all paragraphs are finding the index correctly. These are noted by a starting index of -1.  
