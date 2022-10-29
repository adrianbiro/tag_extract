import sys
from pathlib import Path
import json

import fitz

def openfile(path_to_pdf_file):
    with fitz.open(path_to_pdf_file) as document:
   #     words_dict = {}
   #     for page_number, page in enumerate(document):
   #         words = page.get_text("XT-(.*)")
   #         words_dict[page_number] = words
   # print(json.dumps(words_dict))
        for pnum, page in enumerate(document):
            wlist = page.get_text_words()
            wlist = page.get_text("json") # da text
            #wlist = page.extractDICT()
            print(pnum, wlist)
            print("\n\n\n")


def main():
    if len(sys.argv) > 1:
        openfile(Path(sys.argv[1]))
    else:
        print(f"Usage:\v python3 {sys.argv[0]} <file.pdf>")
        exit(2)

main()
