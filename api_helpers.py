import requests

BASE_URL_DEV= 'http://localhost:3000'

def get_token_and_id(cred):
    """ Returns the Authorization token for a user """
    _token = requests.post(BASE_URL_DEV + '/users/login', cred)
    token = _token.json()[unicode('token')]
    _id = _token.json()[unicode('id')]
    return [token, _id]

def upload_bucket(bucket_data, HEADERS, files):
    resp = requests.post(BASE_URL_DEV + '/upload/bucket', headers=HEADERS, data=bucket_data, files=files)
    return resp.text
