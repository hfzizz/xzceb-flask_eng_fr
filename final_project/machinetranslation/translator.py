import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator('Wok9a6XhmuHzgoJFRMaBAl5Ewyr2TPtxvnYM8klsFtb5')
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url('https://api.jp-tok.language-translator.watson.cloud.ibm.com/instances/2b980df7-bcaf-476e-8d60-61bfb91b80a4')

def english_to_french(english_text):
    """
    This function translates english to french.
    """
    translation = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    This function translates french to english.
    """
    translation = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    english_text = translation['translations'][0]['translation']
    return english_text






