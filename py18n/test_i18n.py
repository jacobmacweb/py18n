import unittest

try:
    from .i18n import I18n
    from .language import Language
except ImportError:
    from i18n import I18n
    from language import Language


class I18nTesting(unittest.TestCase):
    def setUp(self) -> None:
        self.i18n = I18n([
            Language("English", "en", {
                "hello": "Hello",
                "goodbye": "Goodbye",
                "english": "English"
            }),
            Language("French", "fr", {
                "hello": "Bonjour",
                "goodbye": "Au revoir",
                "francais": "Français"
            }),
        ], fallback="en")
    
    def test_basic_get(self):
        self.assertEqual(self.i18n.get_text("hello", "en"), "Hello")
        self.assertEqual(self.i18n.get_text("hello", "fr"), "Bonjour")
        self.assertEqual(self.i18n.get_text("francais", "fr"), "Français")
    
    def test_fallback(self):
        self.assertEqual(self.i18n.get_text("english", "fr"), "English")
        with self.assertRaises(KeyError):
            self.i18n.get_text("english", "fr", should_fallback=False)
    

if __name__ == '__main__':
    unittest.main(verbosity=2)
