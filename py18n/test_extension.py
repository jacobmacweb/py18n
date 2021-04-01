# Copyright (C) 2021 Avery
# 
# This file is part of py18n.
# 
# py18n is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# py18n is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with py18n.  If not, see <http://www.gnu.org/licenses/>.

import unittest

try:
    from .extension import I18nExtension, _
    from .language import Language
except ImportError:
    from extension import I18nExtension, _
    from language import Language


class I18nTesting(unittest.TestCase):
    def setUp(self) -> None:
        self.i18n = I18nExtension([
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
    
    def test_basic_get_contextual(self):
        self.i18n.set_current_locale("en")
        self.assertEqual(_("hello"), "Hello")
        self.i18n.set_current_locale("fr")
        self.assertEqual(_("hello"), "Bonjour")
    
    def test_no_i18n_set(self):
        # Manually get rid of it
        I18nExtension.default_i18n_instance = None
        with self.assertRaises(NameError):
            _("hello")
    

if __name__ == '__main__':
    unittest.main(verbosity=2)
