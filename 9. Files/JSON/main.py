import json


animals = [
    {
        'type': 'rabbit',
        'name': 'Katia',
        'm': 2
    },
    {
        'type': 'lion',
        'name': 'Grisha',
        'm': 21,
        'is_alive': True
    },
]

string = json.dumps(animals)
struct = json.loads(string)

print(struct == animals)
