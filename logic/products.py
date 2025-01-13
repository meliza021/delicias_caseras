import json 

def findAll():
    with open("data/products.json", "r") as file: 
        data = file.read()
        converted = json.loads(data)  
        return converted




