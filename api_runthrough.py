from api_helpers import get_token_and_id, upload_bucket

import sys
files = {'file': open('addresses.csv', 'rb')}
try:
    EMAIL = sys.argv[1]  # Hard Code username here if you do not wish to enter it on the command line
    PASSWD = sys.argv[2] # Hard Code password here if you do not wish to enter it on the command line
except IndexError:
    print 'Usage:\n\n  python api_runthrough.py <email> <password>'
    sys.exit()

CRED = {
    "username": EMAIL,
    "password": PASSWD
    }

user_data = get_token_and_id(CRED)
HEADERS = {
    "Authorization": "Bearer " + user_data[0]
    }

# Create a bucket

bucket_data = {
    "name": "Test Bucket",
    "type": 10,
    "orgId": "acme"
}

print "\nUpload Bucket (addresses):"
print "Here we take a sample csv (testcsv.csv) and upload it to the portal."
print "\nPOST https://api-dev.eltoro.com/upload/bucket"
print "{\n  \"name\": \"Test Bucket\"\n  \"type\": 10\n  \"file\": <file to upload>\n}\n"

print "The response is the id of the created Bucket object"
bucket_resp = upload_bucket(bucket_data, HEADERS, files)
print bucket_resp


