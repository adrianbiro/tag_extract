import sys
from pathlib import Path
import json

import fitz

def openfile(path_to_pdf_file):
    with fitz.open(path_to_pdf_file) as document:
        words_dict = {}
        for page_number, page in enumerate(document):
            words = page.get_text("XT-(.*)")
            words_dict[page_number] = words
            final = fitz.TextPage.extractDICT(words_dict)
    print(json.dumps(final))


def main():
    if len(sys.argv) > 1:
        my_file = sys.argv[1]
        openfile(Path(sys.argv[1]))
    else:
        print(f"Usage:\v python3 {sys.argv[0]} <file.pdf>")
        exit(2)

main()
