import requests
import json
import time
response = requests.get('https://official-joke-api.appspot.com/random_joke')
json_data = json.loads(response.text)
startOfJoke = json_data['setup']
endOfJoke = json_data['punchline']
print(startOfJoke)
time.sleep(3)
print(endOfJoke)