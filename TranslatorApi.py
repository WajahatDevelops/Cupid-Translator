import json, requests, uuid
import supported_languages
import os


class TranslatorApi:
    def __init__(self):
        languages = supported_languages.SupportedLanguages
        self.key1 = os.environ["cognitive_key"]
        self.supported_language_codes = {
            languages.Hindi: "hi",
            languages.Spanish: "es",
            languages.English: "en",
            languages.German: "de",
            languages.French: "fr",
            languages.Russian: "ru",
            languages.Portuguese: "pt",
            languages.Japanese: "ja"
        }
        self.translate_url = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to='
        self.headers = {
            'Ocp-Apim-Subscription-Key': self.key1,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

    def translate(self, text, lang_to):
        code = self.get_lang_code(lang_to)
        
        response = requests.post(self.translate_url+code, str(text).encode('utf-8'), headers=self.headers)
        
        return response

    def get_lang_code(self,language):
        return self.supported_language_codes.get(language, None)

