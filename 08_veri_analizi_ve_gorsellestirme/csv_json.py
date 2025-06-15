import json
data = {'ad': 'Ali', 'yas': 25}
with open('veri.json', 'w') as f:
    json.dump(data, f)