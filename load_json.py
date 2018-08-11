import json

with open('example.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(type(data))