import sys
from pathlib import Path
import json
import fitz
import re

def openfile(path_to_pdf_file):
    regex = "XT-(.*)"
    with fitz.open(path_to_pdf_file) as document:
        final_list = []
        for pnum, page in enumerate(document):
            #wlist = page.get_text("json")
            full_dict = page.get_text("dict")
            page_num = {"page_num": pnum}
            width = {"width": full_dict["width"]}
            height= {"height": full_dict["height"]}
            for b in full_dict["blocks"]:
                if "lines" in b:
                    for l in b["lines"]:
                        for s in l["spans"]:
                            if re.match(regex, s["text"]):
                                text = {"text": s["text"]}
                                coor = {
                                    "x":s["origin"][0],
                                    "y":s["origin"][1]}
                                final = [
                                    page_num,
                                    width,
                                    height,
                                    text,
                                    coor]
                                final_list.append(final)
    return json.dumps(final_list)

def main():
    if len(sys.argv) > 1:
        print(openfile(Path(sys.argv[1])))
    else:
        print(f"Usage:\vpython3 {sys.argv[0]} <file.pdf>")
        exit(2)

main()

# jq '.blocks[].lines[].spans[] | select(.text |test("XT-(.*)"))' full.json
