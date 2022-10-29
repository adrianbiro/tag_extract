from pathlib import Path
from typing import Iterable, Any
import json
import sys
from pdfminer.high_level import extract_pages


def show_ltitem_hierarchy(o: Any, depth=0):
    """Show location and text of LTItem and all its descendants"""
    #if depth == 0:
    #    print('element                        x1  y1  x2  y2   text')
    #    print('------------------------------ --- --- --- ---- -----')
# zmana
    #if o.__class__.__name__ != "LTChar":
    if True:
        #print(
            #f'{get_indented_name(o, depth):<30.30s} '
            #f'{get_optional_bbox(o)} '
            #f'{get_optional_text(o)}'
            #o.__dict__
            #.LTTextLineHorizontal
        #)
        full_list = [int(i) for i in get_optional_bbox(o).split(" ") if len(i)>0]
        my_dict.update({get_optional_text(o): full_list[:2]})


        if isinstance(o, Iterable):
            for i in o:
                show_ltitem_hierarchy(i, depth=depth + 1)


def get_indented_name(o: Any, depth: int) -> str:
    """Indented name of LTItem"""
    return '  ' * depth + o.__class__.__name__


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

######
my_dict = {}
def main():
    if len(sys.argv) > 1:
        my_file = sys.argv[1]
        path = Path(sys.argv[1])
    else:
        print(f"Usage:\v python3 {sys.argv[0]} <file.pdf>")
        exit(2)
    #path = Path('~/gits/pdfPY/market-old.pdf').expanduser()
    #path = Path('~/gits/pdfPY/simple1.pdf').expanduser()

    pages = extract_pages(path)
    show_ltitem_hierarchy(pages)
    #print(my_dict)
    select_dict = {}
    for k, v in my_dict.items():
        if "Prague" in k:
            select_dict.update({k:v})
    print(json.dumps(select_dict))

if __name__ == "__main__":
    main()
