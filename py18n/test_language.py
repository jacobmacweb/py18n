import unittest
from language import Language

class LanguageTesting(unittest.TestCase):
    def setUp(self) -> None:
        self.language = Language("English", "en", {
            "you_lost": "You lost the {game}",
            "game": "game",
            "hello": "Hello, {place}!"
        })
    
    def test_basic_get(self):
        self.assertEqual(self.language.get_text("hello", place="World"), "Hello, World!")
    
    def test_templated(self):
        self.assertEqual(self.language.get_text("you_lost"), "You lost the game")
    
    def test_templated_priority(self):
        self.assertEqual(self.language.get_text("you_lost", game="lottery"), "You lost the lottery")


if __name__ == '__main__':
    unittest.main(verbosity=2)