import json
from formula.logic.products import updateQuantityInventory
def findAll():
    with open("data/products.json", "r") as file:
        data = file.read() #Read es para hacerlo un string
        converted = json.loads(data) #Lo convierte a estructura de datos
        return converted
        convertListOrDict = json.loads(data) #Lo convierte a estructura de datos
        return convertListOrDict
def saveAll(data):
    with open("data/products.json", "w", encoding="utf-8") as file:
        str(data).encode('utf-8')
        convertJson = json.dumps(data, indent=4, ensure_ascii=False)
        file.write(convertJson)
        return "Se modificó el archivo products.json"
def updateInventoryByCode(product_code):
    data = findAll()
    for product in data:
        if(product.get("codigo_producto") == product_code):
            quantity = int(input("Ingrese la cantidad de productos que desea actualizar: "))
            stock = updateQuantityInventory(product.get("cantidad_en_stock"), quantity)
            product.update({"cantidad_en_stock": stock})
            print(f"Se actualizó el {product_code} a {stock}")
    print(saveAll(data))
import json

def newproducts(codigo_producto, nombre, categoria, descripcion, proveedor, cantidad_en_stock, precio_venta, precio_proveedor):
    products = findAll()
    new_product = {
        "codigo_producto": codigo_producto,
        "nombre": nombre,
        "categoria": categoria,
        "descripcion": descripcion,
        "proveedor": proveedor,
        "cantidad_en_stock": cantidad_en_stock,
        "precio_venta": precio_venta,
        "precio_proveedor": precio_proveedor
    }
    products.append(new_product)
    with open("data/products.json", "w") as file:
        json.dump(products, file, indent=4)
    print("Producto guardado correctamente.")

 