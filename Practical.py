###################################################################################################

# modules

from bs4 import BeautifulSoup
from urllib import request
import re
import os
import sys


###################################################################################################

# check if path exists. if not, create path.
try:
    os.mkdir ("C:\\Practical")

except FileExistsError:
    pass
    
###################################################################################################

# functions


# creates html source document
def make_Text_src (url, doc_path):

# create source document
# returns beautifulsoup html source

    doc = open (doc_path, 'w')

    content = request.urlopen (url)

    htmlSource = content.read()

    doc_source = BeautifulSoup (htmlSource, 'html.parser')

    doc.write (doc_source.prettify())

    doc.close

    return doc_source


# pulls text from html that contains searchable string
# returns list
def extract_text_by_string (source, string):

    paragraphs = []

    # find all tags with '$' in text string, exclude 
    for tag in source.find_all (string=re.compile(string)):

    
        # exclude table data
        if len (tag.find_parents("table")) > 0:
            continue
        else:
            paragraphs.append (tag)

    return paragraphs

# creates output file. compares list from extract_text_by_string() and compares to document.txt
def create_indexed_list (inFile, outFile, list):

    lines_to_write = []

    for item in list:

        input = open(inFile, 'r')
        output = open (outFile, 'w')

        text = input.read()

        start = text.find (item)
        end = start + len(item)

        lines_to_write.append ("{\n\t'text': '" + item + "',\n\t'start': '" + str(start) + "',\n\t'end': '" + str(end) + "',\n},\n")

    output.writelines(lines_to_write)

    input.close()
    output.close()


        



# ----------------------------------------------------------------------------------------------- #

def main():


    site = sys.argv[1] #"http://goo.gl/UL5o31"

    document = "C:/Practical/document.txt"

    paragraphs = "C:/Practical/paragraphs.txt"

    str = sys.argv[2] #"\$"

    print ("begin")

    doc_source = make_Text_src (site, document)

    result_set = extract_text_by_string (doc_source, str)

    create_indexed_list (document, paragraphs, result_set)

    print ("end")

# ----------------------------------------------------------------------------------------------- #



main()
