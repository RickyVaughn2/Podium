import requests
import argparse

# Input arg (should be google key and address you are wanting the reps for)
parser = argparse.ArgumentParser()
parser.add_argument('-k', '--key', help='google api key', required=True)
parser.add_argument('-a', '--address', help='address to search', required=True)
args = parser.parse_args()

query = {'key': args.key, 'address': args.address}
url = 'https://www.googleapis.com/civicinfo/v2/representatives'
req = requests.get(url, params=query)

print(req.status_code)
# print(req.json())
print(req.text)
