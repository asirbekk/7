import json

data = {}
data['people'] = []
data['people'].append({
    'товар': 'add',
    'магазин': 'add',
    'стой': 'Uzbekiston'
})
print(data)


with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)