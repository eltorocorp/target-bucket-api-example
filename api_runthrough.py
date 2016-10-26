from api_helpers import get_token_and_id
import sys


try:
    EMAIL = sys.argv[1]  # Hard Code username here if you do not wish to enter it on the command line
    PASSWD = sys.argv[2] # Hard Code password here if you do not wish to enter it on the command line
except IndexError:
    print 'Usage:\n\n  python api_runthrough.py <email> <password>'
    sys.exit()

CRED = {
    "email": EMAIL,
    "password": PASSWD
    }

user_data = get_token_and_id(CRED)

print user_data
