import unittest
from wordle import LetterColour, WordleGame

class TestLetterColour(unittest.TestCase):
    def test_letter_colour(self):
        letter = 'A'
        colour = 'red'
        letter_colour = LetterColour(letter, colour)
        
        self.assertEqual(letter_colour.letter, letter)
        self.assertEqual(letter_colour.colour, colour)

class TestWordleGame(unittest.TestCase):
    def test_init(self):
        word = "apple"
        game = WordleGame(word)
        
        self.assertEqual(game.word, word)
        self.assertEqual(game.num_guesses, 0)
        self.assertEqual(game.max_guesses, 6)
    
    def test_play(self):
        word = "apple"

        
        # Test correct guess
        game = WordleGame(word)
        
        game.play("apple")
        self.assertEqual(game.num_guesses, 1)
        self.assertEqual(game.correct_letters, 5)
        self.assertEqual(game.contained_letters, 0)
        self.assertEqual(game.incorrect_letters, 0)
        self.assertFalse(game.game_over)
        self.assertTrue(game.won)
        
        
        # Test incorrect guess
        game = WordleGame(word)
        
        game.play("bunny")
        self.assertEqual(game.num_guesses, 6)
        self.assertEqual(game.correct_letters, 0)
        self.assertEqual(game.contained_letters, 0)
        self.assertEqual(game.incorrect_letters, 5)
        self.assertTrue(game.game_over)
        self.assertFalse(game.won)
        
        
        game = WordleGame(word)
        
        game.play("night")
        self.assertEqual(game.num_guesses, 6)
        self.assertEqual(game.correct_letters, 0)
        self.assertEqual(game.contained_letters, 0)
        self.assertEqual(game.incorrect_letters, 5)
        self.assertTrue(game.game_over)
        self.assertFalse(game.won)
        
        # Test contained letters
        game = WordleGame(word)
        
        game.play("pelap")
        
        self.assertEqual(game.num_guesses, 6)
        self.assertEqual(game.correct_letters, 0)
        self.assertEqual(game.contained_letters, 5)
        self.assertEqual(game.incorrect_letters, 0)
        self.assertTrue(game.game_over)
        self.assertFalse(game.won)
        
        
        game = WordleGame(word)
        
        game.play("paple")
        self.assertEqual(game.num_guesses, 6)
        self.assertEqual(game.correct_letters, 3)
        self.assertEqual(game.contained_letters, 2)
        self.assertEqual(game.incorrect_letters, 0)
        self.assertTrue(game.game_over)
        self.assertFalse(game.won)
    
    
    def test_input_word(self):
        
        # Test input word with correct length
        word = "apple"
        game = WordleGame(word)
        game.play("apple")
        self.assertEqual(game.num_guesses, 1)
        self.assertEqual(game.correct_letters, 5)
        self.assertEqual(game.contained_letters, 0)
        self.assertEqual(game.incorrect_letters, 0)
        self.assertFalse(game.game_over)
        self.assertTrue(game.won)
        
        
        # Test input word with incorrect length
        word = "apple"
        game = WordleGame(word)
        game.play("apples")
        self.assertEqual(game.num_guesses, 0)
        self.assertEqual(game.correct_letters, 0)
        self.assertEqual(game.contained_letters, 0)
        self.assertEqual(game.incorrect_letters, 0)
        self.assertFalse(game.game_over)
        self.assertFalse(game.won)
        
        game.play("app")
        self.assertEqual(game.num_guesses, 0)
        self.assertEqual(game.correct_letters, 0)
        self.assertEqual(game.contained_letters, 0)
        self.assertEqual(game.incorrect_letters, 0)
        self.assertFalse(game.game_over)
        self.assertFalse(game.won)
        
        
    
    def test_display_word(self):
        word = "apple"
        game = WordleGame(word)
        guesses = ["paple", "ladel", "night", "apple"]
        

        # Test displaying word with half correct guesses
        self.assertEqual(game.display_word(guesses[0], True), "paPLE")
        self.assertEqual(game.display_word(guesses[1], True), "la_el")
        
        # Test displaying word with INcorrect guesses
        self.assertEqual(game.display_word(guesses[2], True), "_____")
        
        # Test displaying word with correct guess
        self.assertEqual(game.display_word(guesses[3], True), "APPLE")
    
        

if __name__ == '__main__':
    unittest.main()
