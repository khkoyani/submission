import requests

# URL = 'http://localhost:8000/?username=testuser'
URL = 'http://localhost:8000/'

# data = {
#     'name': 'Burger2',
#     'user': 1,
#     'steps': [
#         {'step_text': 'Add ingredient 1'},
#         {'step_text': 'Add other stuff'}
#     ],
#     'ingredients': [
#         {'ingredient': 'Bread'},
#         {'ingredient': 'Meat'},
#     ]}

data = {
        'name': 'pizza',
        'steps': [
            {'id': 5, 'step_text': 'updated step again'},
            {'step_text': 'Add other stuff'}
        ],
        'ingredients': [{'id': 4, 'ingredient': 'testing Meat'}, {'id': 5, 'ingredient': 'test Cheese'}]
    }


def req(data):
    r = requests.patch(URL, json=data)
    print(r.json())



print(requests.get(URL).json())

print('--------------------')

# req(data=data)
print(requests.get(URL).json())

