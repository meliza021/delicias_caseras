from logic.products import findAll as findAllProducts
from logic.order import findAllOrders, saveAll, findAllProducts as findAllProducts1
from tabulate import tabulate
from datetime import datetime
import random
def desing():
    print("""
   _*_ *_*__*__*__*__*__*__*__*__*__*__*__*_    
   _*_          El menu                  _*_
   _*_ 1. Realizar pedido de producto    _*_
   _*_ 2. Ver pedidos realizados         _*_
   _*_ 0. salir                          _*_
    *_*__*__*__*__*__*__*__*__*__*__*__*__*_
    """)
    opc = int(input())
    return opc 

def formularyTakeOrder():
    dataProducts =findAllProducts()
    dataOrders = findAllOrders()
    now = datetime.now()
    findproductsMajo = list(filter(lambda product: product.get ("cantidad_en_stock") > 0 , dataProducts))
    findproducts = list(filter(lambda product:(product.pop("categoria"), product.pop("proveedor"), product.pop("precio_proveedor")),findproductsMajo)