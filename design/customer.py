from logic.products import findAll as findAllProducts
from logic.order import findAll as findAllOrders
from tabulate import tabulate
from datetime import datetime

def desing():
    print("""
    Menu de clientes
        0. Salir
        1. Realizar pedido
        2. Ver pedidos realizados
    """)
    opc = int(input())
    return opc

def formularyTakeOrder():
    dataProducts = findAllProducts()
    dataOrders = findAllOrders()
    findProductsMajor = list(filter(lambda product: product.get("cantidad_en_stock") > 0, dataProducts))
    findProducts = list(filter(lambda product: (product.pop("descripcion"), product.pop("proveedor"), product.pop("precio_proveedor")), findProductsMajor))
    print("Lista de productos disponibles")
    print(tabulate(findProducts, headers= "keys", tablefmt="grid", numalign="center", showindex="always"))
    now = datetime.now()
    format = now.strftime('%Y-%m-%d')
    for indice, product in enumerate(dataOrders):
        dataOrders[indice] = product.get("codigo_pedido")
        #dataOrders = list(dataOrders[-1].get("codigo_pedido"))
        return dataOrders
    
    formulary = dict({
        "codigo_pedido": dataOrders[-1] + 1,
        "codigo_cliente": input("Codigo del cliente, ejeplo (CL-001): "),
        "fecha_pedido": format,
        "detalles_pedido": [],
    })