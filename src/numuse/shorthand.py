import re

class RIC_Shorthand:
    """This class allows rooted interval collections to be written quickly"""

    def __init__(self, RIC_Shorthand: str):
        self.RIC_Shorthand = RIC_Shorthand

    def parse_RIC_shorthand(self, RIC_Shorthand):
        """Converts RIC shorthand to a root and set of notes"""


    def parse_RIC_shorthand_unit(self, RIC_Shorthand_unit) -> int:
        """Given a unit of RIC shorthand, we convert it to an interval"""

        # It will always have a digit
        d = re.search(r"[0-9R]+", RIC_Shorthand_unit)
        found = RIC_Shorthand_unit[d.start() : d.end()]
        if found == "R":
            digit = None
        else:
            digit = int(found)

        m = re.search(r"[,'ud]", RIC_Shorthand_unit)

        if m:
            direction = RIC_Shorthand_unit[m.start()]
            count = len(RIC_Shorthand_unit[m.start() :])
            multiplier = -1 if direction in ["d", ","] else 1

            return digit + multiplier * count * 12
        else:
            return digit
