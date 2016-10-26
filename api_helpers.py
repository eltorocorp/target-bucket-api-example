import requests

BASE_URL_DEV= 'https://api-dev.eltoro.com'

def get_token_and_id(cred):
    """ Returns the Authorization token for a user """
    _token = requests.post(BASE_URL_DEV + '/users/login', cred)
    token = _token.json()[unicode('token')]
    _id = _token.json()[unicode('id')]
    return [token, _id]
