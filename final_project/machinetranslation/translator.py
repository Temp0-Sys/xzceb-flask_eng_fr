"""
ibm_watson and ibm_cloud)sdk_core.authenticators are required in order to use IBM Watson translator
os allows us to access  the apikey and url that stored in the .env file
dotenv loads the env file to be readable
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()


apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """Getting text in english, Passing it to IBM Watson Translator, returns in french"""
    translation = language_translator.translate(
       text=english_text,
       model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """translating text from french to english"""
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
