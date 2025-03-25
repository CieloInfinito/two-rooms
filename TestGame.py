import unittest
from Game import Game  
from PlayingCharacters import PlayingCharacters

class TestGame(unittest.TestCase):
    def setUp(self):
        self.pc = PlayingCharacters()
        self.game = Game(self.pc.characters)

    def test_card_add_to_deck(self):
        self.game.add_card_to_deck(self.pc.no_15)
        self.assertIn(self.pc.no_15, self.game.deck)

    def test_resolve_turn_with_harman_results_fuga(self):
        self.game.red_room.extend([self.pc.no_15, self.pc.no_6, self.pc.no_14, self.pc.no_17])  
        result = self.game.resolve_turn(self.game.red_room)
        self.assertEqual(result, "FUGA")

    def test_resolve_turn_no_injury(self):
        self.game.red_room.extend([self.pc.no_15, self.pc.no_14])  
        result = self.game.resolve_turn(self.game.red_room)
        self.assertEqual(result, "SILENCIO")