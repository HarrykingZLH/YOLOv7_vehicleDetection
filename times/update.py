import json

data = {}

with open('time_file.json', 'w') as file:
    json.dump(data, file, indent=4)

print('finish!')