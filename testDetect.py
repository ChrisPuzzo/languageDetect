import detectlanguage

from langaugeDetect import LanguageCalls

detectlanguage.configuration.api_key = "8df729e6c77caed3593ca12c940683ee"


kanji = LanguageCalls('漢字').languageDecetion()

print(kanji)
