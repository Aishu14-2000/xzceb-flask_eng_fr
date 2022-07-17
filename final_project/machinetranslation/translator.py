"""
load modules
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#Enable Authenticator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

#English to French Translation
def english_to_french(englishtext):
    """
    Function translates text from English to French
    """
    frenchtext = language_translator.translate(englishtext,model_id='en-fr').get_result()
    frenchtext = frenchtext['translations'][0]['translation']
    return frenchtext

#French to English Translation
def french_to_english(frenchtext):
    """
    Function translates text from French to English
    """
    englishtext = language_translator.translate(frenchtext,model_id='fr-en').get_result()
    englishtext = englishtext['translations'][0]['translation']
    return englishtext