import sys
from pathlib import Path
import json
import fitz
#import pyjq  #TODO nechce ho nainštalovať

def openfile(path_to_pdf_file):
    with fitz.open(path_to_pdf_file) as document:
        for page in document:
            wlist = page.get_text("json")
            #selected_jason = pyqj.first('.blocks[].lines[].spans[] | select(.text |test("XT-(.*)"))', wlist)
            #print(selected_jason)
            print(wlist)


def main():
    if len(sys.argv) > 1:
        openfile(Path(sys.argv[1]))
    else:
        print(f"Usage:\v python3 {sys.argv[0]} <file.pdf> | jq '.blocks[].lines[].spans[] | select(.text |test(\"XT-(.*)\"))'")
        exit(2)

main()

# jq '.blocks[].lines[].spans[] | select(.text |test("XT-(.*)"))' full.json
