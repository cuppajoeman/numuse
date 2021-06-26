import re
from typing import Tuple, Set

def parse_RIC_shorthand(RIC_shorthand: str) -> Tuple[int, Set[int]]:
    """Converts RIC shorthand to a root and set of notes"""
    str_root, str_intervals = RIC_shorthand.split('|')
    root = int(str_root)
    intervals = {parse_RIC_shorthand_unit(unit) for unit in str_intervals.split(' ')}
    return root, intervals

def parse_RIC_shorthand_unit(RIC_shorthand_unit: str) -> int:
    """Given a unit of RIC shorthand, we convert it to an interval"""

    # It will always have a digit
    d = re.search(r"[0-9R]+", RIC_shorthand_unit)
    found = RIC_shorthand_unit[d.start() : d.end()]

    digit = int(found)

    # octave displacement
    m = re.search(r"[,'ud]", RIC_shorthand_unit)

    if m:
        direction = RIC_shorthand_unit[m.start()]
        count = len(RIC_shorthand_unit[m.start() :])
        multiplier = -1 if direction in ["d", ","] else 1

        return digit + multiplier * count * 12
    else:
        return digit
