import json
def findAll():
    #python ABRE el archivo y luego lo lee "r = read"
    with open("data/products.json", "r") as file:
        data = file.read() #String
        converted =json.loads(data)
        return converted