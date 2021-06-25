from __future__ import annotations
from tools import *
from typing import Set, Dict
from musical_system import RBMS_Approximation
from constants import JUST_INTONATION_RATIOS, JAZZ_INTERVAL_COLLECTIONS

class NoteCollection:
    """A collection of notes from a musical system

    Attributes
    ----------
    notes: List[int]
      the notes in this note collection

    Methods
    -------
    __eq__(other_NC: NoteCollection)
      Checks whether this note collection is the same as the other one

    generate_wave_function(self)
      Generates the wave function determined by the current musical system
      As of right now this is assumed to be 12 tone equal temperament

    compute_diatonic_distance(self, other_NC: NoteCollection):
      Return how many notes the two note collections differ by

    """

    def __init__(self, notes: set):
        self.notes = notes

    def __eq__(self, other_NC):
        """True if they contain the same notes"""
        return self.notes == other_NC.notes

    def generate_wave_function(self):
        raise NotImplementedError

    def compute_diatonic_distance(self, other_NC: NoteCollection) -> float:
        """Return how many notes the two note collections differ by"""
        raise NotImplementedError


class RootedIntervalCollection(NoteCollection):
    """A note collection instantiated in a special way

    A rooted interval collection is a way to define a
    set of notes of a musical system.

    It does so specifying a note (denoted by root) from the system and
    a set of intervals measured with respect to the root.
    """

    def __init__(
        self,
        root: int,
        interval_collection: Set[int],
        duration=0,
        musical_system=RBMS_Approximation(
            440, JUST_INTONATION_RATIOS, 2, 2 ** (1 / 12), 12
        ),
    ):
        """
        durations is measured in seconds, it is by default set to 0 seconds to represent no duration
        """
        self.musical_system = musical_system
        self.root = root
        self.interval_collection = interval_collection
        super().__init__(self.generate_notes(self.root, self.interval_collection))

    def generate_notes(self, root, interval_collection) -> Set[int]:
        """Generate the notes that are defined by taking the root note and adding
        the notes in the interval collection"""
        return {root + x for x in interval_collection}

    def compute_intervallic_complexity(self) -> float:
        interval_to_occurance = self.generate_interval_to_occurance()
        intervallic_complexity = 0
        for interval, occurance in interval_to_occurance.items():
            #ratio = self.musical_system.interval_to_ratio[interval]
            #ratio = self.musical_system.interval_to_ratio[interval]
            #ratio_complexity = self.musical_system.ratios_to_complexity[ratio] * occurance
            interval_complexity = self.musical_system.interval_to_complexity[interval] * occurance
            intervallic_complexity += interval_complexity
        return intervallic_complexity

    def generate_interval_to_occurance(self) -> Dict[int, int]:
        """Generate a dictionary that maps all possible intervals in this interval collection to the number of times it appears"""
        num_intervals = len(self.interval_collection)
        fixed_order_interval_collection = sorted(list(self.interval_collection))
        interval_to_occurance = {}
        for i in range(num_intervals):
            for j in range(i, num_intervals):
                if i < j:
                    interval_a = fixed_order_interval_collection[i]
                    interval_b = fixed_order_interval_collection[j]
                    interval_between = I(interval_a, interval_b)
                    fundamental_interval_between = ranged_modulus_operator(
                        interval_between, self.musical_system.num_notes
                    )
                    if interval_between not in interval_to_occurance:
                        interval_to_occurance[fundamental_interval_between] = 1
                    else:
                        interval_to_occurance[fundamental_interval_between] += 1
        return interval_to_occurance

    def get_fundamental_representation(self) -> RootedIntervalCollection:
        """Generate the fundamental representation of this interval collection

        The fundamental representation a rooted interval collection where the interval
        are within the range 0 ... num_notes - 1 where num_notes is defined by the
        musical system we are dealing with.

        In 12 tone equal temperament, num_notes is equal to 12.

        Example:
            If we have a rooted interval collection 13 | -3 1 2 24

        """
        fundamental_interval = {
            ranged_modulus_operator(i, self.musical_system.num_notes)
            for i in self.interval_collection
        }
        fundamental_root = ranged_modulus_operator(
            self.root, self.musical_system.num_notes
        )
        return RootedIntervalCollection(fundamental_root, fundamental_interval)


if __name__ == "__main__":
    C7 = RootedIntervalCollection(0, {0, 4, 7, 11})
    for interval_collection in JAZZ_INTERVAL_COLLECTIONS:
        chord = RootedIntervalCollection(0, interval_collection)
        print(interval_collection)
        #print(chord.musical_system.ratios_to_complexity)
        print(chord.compute_intervallic_complexity())
