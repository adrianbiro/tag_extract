from pathlib import Path
from typing import Iterable, Any
import json
from pdfminer.high_level import extract_pages


def show_ltitem_hierarchy(o: Any, depth=0):
    """Show location and text of LTItem and all its descendants"""
    if depth == 0:
        print('element                        x1  y1  x2  y2   text')
        print('------------------------------ --- --- --- ---- -----')
# if
    #if o.__class__.__name__ != "LTChar":
    if True:
        print(
            f'{get_indented_name(o, depth):<30.30s} '
            f'{get_optional_bbox(o)} '
            f'{get_optional_text(o)}'
            #o
            #.LTTextLineHorizontal
        )

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


path = Path('~/gits/pdfPY/pokus10.pdf').expanduser()
#path = Path('~/gits/pdfPY/market-old.pdf').expanduser()
#path = Path('~/gits/pdfPY/simple1.pdf').expanduser()

pages = extract_pages(path)
show_ltitem_hierarchy(pages)
