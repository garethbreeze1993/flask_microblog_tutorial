import json
import requests
from flask_babel import _
from flask import current_app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error the translation service is not configured')
    data = [{'Text': text}]
    data_length_json = json.dumps(data)
    length_of_body = len(data_length_json.encode('utf-8'))
    auth = {'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY'], 'Ocp-Apim-Subscription-Region': 'westeurope',
            "Content-Type": "application/json; charset=UTF-8"}
    r = requests.post('https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to={}&from={}'.format(
        dest_language, source_language),
        headers=auth, data=data_length_json)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    python_response = json.loads(r.content.decode('utf-8-sig'))  # returns list
    translated_text = python_response[0].get('translations')[0].get('text')
    return translated_text

# json loads turns json into python r.content returns bytes s needs to be decoded
