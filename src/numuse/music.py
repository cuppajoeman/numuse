from typing import List, Tuple
from fractions import Fraction

class Music:
    """Represents notes that are played over time"""
    def __init__(self, music_data: List[Tuple[List[int], List[Fraction]]]):
        self.music_data = music_data

    def generate_song_points(self):
        """Generates points of the form (moment, note(s)??, duration)

        TODO: make this work for chords too

        """
        current_time = 0
        song_points = []
        for measure in self.music_data:
            notes, rhythms = measure
            note_to_rhythm = zip(notes, rhythms)
            for n, r in note_to_rhythm:
                if n is not None:
                    # This defines the format
                    song_points.append((current_time, n, r))
                current_time += r
        return song_points

