"translator between french and english"
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    "Translates english to french"
    french_text = MyMemoryTranslator(source = 'en-US', target = 'fr-FR').translate(english_text)
    return french_text

#print(english_to_french("hello"))

def french_to_english(french_text):
    "Translates french to english"
    english_text = MyMemoryTranslator(source = 'fr-FR', target = 'en-US').translate(french_text)
    return english_text

#print(french_to_english("bonjour"))
