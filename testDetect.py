import detectlanguage

from langaugeDetect import LanguageCalls

detectlanguage.configuration.api_key = "8df729e6c77caed3593ca12c940683ee"


print(LanguageCalls('漢字').simpleOutput())