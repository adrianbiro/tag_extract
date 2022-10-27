from pathlib import Path
from typing import Iterable, Any
import json
import sys
from pdfminer.high_level import extract_pages

def show_ltitem_hierarchy(o: Any, depth=0):
    full_list = [int(i) for i in get_optional_bbox(o).split(" ") if len(i)>0]
    #TODO or FIXME swap dict or make list of dict with counter "k" then dump all json to jq
    my_dict.update({get_optional_text(o): full_list[:2]})

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
    show_ltitem_hierarchy(pages)
    select_dict = {k:v for k, v in my_dict.items() if string_to_find in k}
    print(json.dumps(select_dict))
    #print(json.dumps(my_dict))

my_dict = {}
string_to_find = "Reason"
#string_to_find = "XTAGNAMEX" #TODO
if __name__ == "__main__":
    main()
