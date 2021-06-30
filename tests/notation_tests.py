import unittest
# Assumes a local install of numuse
from numuse.notation import Note, NoteCollection

class TestNote(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(Note(1), Note(1))

    def test_octave(self):
        self.assertEqual(Note(24).octave_offset, 2)

    def test_name(self):
        self.assertEqual(Note(24).note_name, 0)

    def test_addition(self):
        self.assertEqual(Note(1) + 1, Note(2))

    def test_subtraction(self):
        self.assertEqual(Note(1) - 1, Note(0))

class TestNoteCollection(unittest.TestCase):
    
    def test_equality(self):
        NC1 = NoteCollection({Note(0), Note(4), Note(7), Note(11)})
        NC2 = NoteCollection({Note(4), Note(0), Note(7), Note(11)})
        self.assertEqual(NC1, NC2)

if __name__ == '__main__':
    unittest.main()
