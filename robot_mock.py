import requests
import datetime

while 1:
    headers = {
        # Already added when you pass json= but not when you pass data=
        # 'Content-Type': 'application/json',
    }

    json_data = {
        'robot': '1',
        'x': '1',
        'y': '1',
        'datetime': str(datetime.datetime.now()),
    }

    response = requests.put('http://127.0.0.1:8000/positions/44/', headers=headers, json=json_data, auth=('admin', 'admin'))

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"robot":"1", "x":"1", "y":"1", "datetime":"2022-04-01T11:11"}'
#response = requests.post('http://127.0.0.1:8000/positions/', headers=headers, data=data, auth=('admin', 'admin'))