from logic.products import findAll
from tabulate import tabulate

def desing():
    print("""
        *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_**_*_*_*_*_*_*_*_*
        *_        Menu                                  _*
        *_ 1. agregar producto                          _*
        *_ 2. ver producto                              _*
        *_ 3. ver producto por categoria                _*
        *_ 4. acualizar el inventario de un producto    _*
        *_ 5.                                           _*
        *_ 0. salir                                     _*
        *_*_*_*_*_*_*_*_*_*_*_*_ *_*_*_*_*_*_*_*_*_*_*_*_*
    """)
    opc = int(input()) 
    return opc
def addProduct():
    data = findAll()
    codeproduct = input("Ingrese el código de producto: ")  
    findProducts = list(filter(lambda product: product.get("codigo_producto") == codeproduct, data))
    print(findProducts)
    
   # formulary = dict({
    #     "codigo_producto": codeproduct,  
     #    "nombre": input("Ingrese el nombre del producto: "),
     #    "categoria": input("Ingrese la categoría del producto: "),
      #   "descripcion": input("Ingrese la descripción del producto: "),
       #  "cantidad_en_stock": input("Ingrese la cantidad en stock del producto: "),
      #   "precio_venta": input("Ingrese el precio de venta del producto: "),
       #  "precio_proveedor": input("Ingrese el precio del proveedor del producto: "),
  #   })

 

def tableProducts():
    data = findAll()  
    codeproduct = input ("ingrese el producto ")
    print("\tTodos los productos\n")  
    indice = 0
    for products in data: 
        print(f'{indice}. {products.get("nombre")} category: {products.get("categoria")} {products.get("precio_venta")}\n')
        indice += 1

def tableProductsBycategory(category):
    data = findAll()
    dataModify = []
    for diccionario in data:
     if (diccionario.get("categoria")==category):
         diccionario.pop("descripcion")
         diccionario.pop("proveedor")
         diccionario.pop("precio_provedor")
         dataModify.append(diccionario)
     print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center", showindex="always"))