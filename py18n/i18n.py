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

from typing import List, Union

try:
    from .language import Language
except ImportError:
    from language import Language


class I18n:
    def __init__(self, languages: List[Language], fallback: Union[str, int]) -> None:
        self._languages = {
            language.code: language
            for language in languages
        }

        self._fallback = None
        if isinstance(fallback, str):
            self._fallback = fallback
            
            if self._fallback not in self._languages:
                raise KeyError(f"No language found with code {fallback} as fallback")
        elif isinstance(fallback, int):
            self._fallback = self._languages[languages[fallback].code]
        
        if self._fallback is None:
            raise KeyError(f"No fallback language set. Check documentation for correct usage")

    def get_text(
        self,
        key: str,
        locale: str,
        list_formatter: bool = None,
        use_translations: bool = True,
        should_fallback: bool = True,
        **kwargs
    ) -> str:
        # Get locale
        if locale not in self._languages:
            raise KeyError(f"Given locale `{locale}` does not exist!")
        language = self._languages[locale]
        
        try:
            result = language.get_text(key, list_formatter=list_formatter, use_translations=use_translations, **kwargs)
        except KeyError as exc:
            # If we shouldn't fallback or this is the fallback
            if not should_fallback or locale == self._fallback:
                raise KeyError(f"Translation {key} not found for {locale}!") from exc
        else:
            return result
        
        # We only get here if fallback is enabled and the text wasn't found in
        # the initial language
        try:
            result = self._languages[self._fallback].get_text(
                key, list_formatter=list_formatter, use_translations=use_translations, **kwargs)
        except KeyError as exc:
            raise KeyError(f"Translation {key} not found for {locale} nor fallback {self._fallback}") from exc
        else:
            return result

