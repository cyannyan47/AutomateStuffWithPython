import json

with open('videoid.json', 'r') as json_file:
  data = json.load(json_file)
  print(data)
