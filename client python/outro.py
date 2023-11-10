
import requests
import json
def get_something():
    token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwaXp6dXJnLWFwaSIsImlhdCI6MTY5OTU4NDU0NiwiZXhwIjoxNjk5NTk4OTQ2LCJzdWIiOiJ0ZXN0ZUBlbWFpbC5jb20ifQ.5EAFe_cvGtgT9f3wzLRj14F1Q5u8O44YQqnw-Qi2ejE"
    headers = {'Authorization': f'Bearer {token}'}
    request = requests.get("http://localhost:8080/api/kaggle/v1/products", headers=headers)
    print("get something: ")
    print("status code response: ", request.status_code)
    print("content response: ", request.content)
    print(type(request))
    data = request.json()
    

    for i in data:
        print("Name:", i['product_name'])

get_something()