import requests
import os
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# curl https://api.twitter.com/2/tweets/sample/stream -H "Authorization: Bearer $BEARER_TOKEN"

print("Connecting")
# 😷


# headers = {
#     'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAADcsIgEAAAAAy1qlVnUMfKAGBV5UQ2h1V7PdliM%3DZmAnxnBehVs1NFQN3Y4gbgpAzYS029WX8J8bBK2YBEGhM3KpyD',
# }
# response = requests.get('https://api.twitter.com/2/tweets/sample/stream', headers=headers)
# print(response)
print("Finished")