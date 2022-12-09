import json
py_data = {'name': 'ajay', 'phone': 9497858477, 'place': 'kollam'}
json_data = json.dumps(py_data)
print(f'Json string : {json_data}')
print(f'value of second key: {json.loads(json_data)["phone"]}')
