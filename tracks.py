import json

favorite_tracks = [
    {'name': 'track 1', 'artist': 'artist1'},
    {'name': 'track 2', 'artist': 'artist2'},
    {'name': 'track 3', 'artist': 'artist3'}
]


with open ('tracks.json', 'w', encoding='utf-8') as f:
    json.dump(favorite_tracks, f)

print('Выполнено')