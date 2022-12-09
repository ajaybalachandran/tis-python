import json
length = int(input('Enter the length of dictionary: '))
py_data = {}
for i in range(1, length+1):
    key = input(f'Enter the key{i}: ')
    value = input(f'Enter the value{i}: ')
    py_data[key] = value
json_data = json.dumps(py_data)
print(f'Json string : {json_data}')
print(f'value of second key: {json.loads(json_data)["phone"]}')
