import json

def findAll():
    with open("data/products.json", "r", encoding="utf-8") as file :
        data = file.read()
        convertedList = json.loads(data)
        return convertedList