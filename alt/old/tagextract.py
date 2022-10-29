from pathlib import Path
from typing import Iterable, Any
import json
import sys
import re
from pdfminer.high_level import extract_pages

page_num = 0
final_dict = {}

class Record:
    def __init__(self, clist, tname):
        """list of coor, text"""
        coordinates = self.clist
        pnum = page_num
        name = self.tname


def show_ltitem_hierarchy(o: Any, depth=0):
    page_num = 1
    if o.__class__.__name__ == "LTPage":
        page_num =+ 1
        print(page_num)
    full_list = [int(i) for i in get_optional_bbox(o).split(" ") if len(i)>0]
    final_dict.update({
        get_optional_text(o): 
        {"tags" : full_list[:], "Pagenum": page_num }
        })

    if isinstance(o, Iterable):
        for i in o:
            show_ltitem_hierarchy(i, depth=depth + 1)

def get_optional_bbox(o: Any) -> str:
    """Bounding box of LTItem if available, otherwise empty string"""
    if hasattr(o, 'bbox'):
        return ''.join(f'{i:<4.0f}' for i in o.bbox)
    return ''

def get_optional_text(o: Any) -> str:
    """Text of LTItem if available, otherwise empty string"""
    if hasattr(o, 'get_text'):
        return o.get_text().strip()
    return ''

def main():
    if len(sys.argv) > 1:
        my_file = sys.argv[1]
        path = Path(sys.argv[1])
    else:
        print(f"Usage:\v python3 {sys.argv[0]} <file.pdf>")
        exit(2)

    pages = extract_pages(path)
    com_dict = {}
    show_ltitem_hierarchy(pages)
    simple_dict = {k:v for k, v in final_dict.items() if re.match('XT-(.*)', k)}
    print(simple_dict)
    #print(json.dumps(simple_dict))
    #print(json.dumps(final_dict))

#page_num = 0
#final_dict = {}
#string_to_find = "XTAGNAMEX"
if __name__ == "__main__":
    main()
