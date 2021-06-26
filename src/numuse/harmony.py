from typing import List, Tuple
from fractions import Fraction

class Music:
    """Represents notes that are played over time"""
    def __init__(self, music_data: List[Tuple[str, List[Fraction]]]):
        self.music_data = music_data
