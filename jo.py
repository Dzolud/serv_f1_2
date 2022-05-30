import requests

print(requests.post('http://localhost:5000/api/add_photo',
                        json={'chat_id': 667,
                              'photo': "male"}))
# print(requests.get('http://localhost:5000/api/get_mf/667'))