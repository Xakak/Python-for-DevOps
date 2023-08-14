import json

people_string ='''
 {
    "people": [
        {
            "name": "Rayan",
            "phone_number": "03315463900",
            "email": ["xakak", "rayan"]

        },
        {
            "name": "Khalid",
            "phone_number": "03006050796",
            "email": false
        }
    ]


}
'''
# json.loads (s stands for string) converts above json string into py compatible:
python_data = json.loads(people_string)
print(python_data)
for person in python_data['people']:
    print(person['email'])

# vice versa to above:
json_data = json.dumps(python_data,indent=2)
print(json_data)

# json.load converts file into py compatible:
with open("states.json",'r') as f:
    states_data = json.load(f)
# create new json file without abbreviation:
for state in states_data:
    del state['abbreviation']
with open("new_states.json", 'w') as f:
    json.dump(states_data, f, indent=2)


