import detectlanguage
import unittest

detectlanguage.configuration.api_key = "8df729e6c77caed3593ca12c940683ee"

# set up classe LangaugeCalls where our langauge functions will be located
class LanguageCalls():
    def __init__(self, uInput):
        self.uInput = uInput

    def detailedOutput(self):
        return detectlanguage.detect(self.uInput)

    def simpleOutput(self):
        return detectlanguage.simple_detect(self.uInput)



class tests(unittest.TestCase):
    
    def test_spanish(self):
        esp = 'Buenos dias señor'
        self.assertEqual('es', LanguageCalls(esp).simpleOutput())

    def test_eng(self):
        en = 'Good morning sir'
        self.assertEqual('en', LanguageCalls(en).simpleOutput())


if __name__ == '__main__':
    unittest.main()