import requests
import json
def get_something():
    json = {
    "email": "teste@email.com",
    "password": "1234"
}
    request = requests.post("http://localhost:8080/api/kaggle/v1/users/login", json=json)
    print("get something: ")
    print("status code response: ", request.status_code)
    print("content response: ", request.content)
    # all_fields = request.json()    
    # print(all_fields)
    data = request.json()
    print(type(data))
    print(data['token'])
 
get_something()