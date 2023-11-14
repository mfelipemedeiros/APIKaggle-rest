
import requests
import json
def get_something():
    token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwaXp6dXJnLWFwaSIsImlhdCI6MTY5OTgzODcwOSwiZXhwIjoxNjk5ODUzMTA5LCJzdWIiOiJ0ZXN0ZUBlbWFpbC5jb20ifQ.ZNfywG46J6iX3b5I8mob_fnQxXiH0lYmTojkCthT6Tk"
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