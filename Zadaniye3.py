import json

with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Товар: ' + p['товар'])
        print('Магазин: ' + p['магазин'])
        print('Стой: ' + p['стой'])
        print('')

