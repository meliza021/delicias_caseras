from design.products import design, tableProducts
from design.products import design, tableProducts, tableProductsByCategory
from logic.products import updateInventoryByCode, newproducts

match design():
    case 1:
        tableProducts()
    case 2:
        tableProductsByCategory(input("Ingrese la categoria. Ejemplo ('panes', 'pastel', 'postres'): "
        ).lower())
    case 3:
        updateInventoryByCode(input("Ingrese el codigo del producto: ") )
    case 4:
        codigo = input("ingrese el codigo_producto ejemplo (PN-001): ")
        nombre = input("ingrese el nombre del producto ejemplo (galletas): ")
        cat = input("ingrese la categoria del producto:  ")
        desc = input("ingrese la descripcio del producto: ")
        prov = input("ingrese el proveedor del producto (Panadería Natural):  ")
        cant_sto = int(input("ingrese la cantidad de stock:  "))
        precio = float(input("ingrese el precio de venta: "))
        precioPro = float(input("ingrese el precio de proveedor: ") )
        newproducts(codigo, nombre, cat, desc, prov, cant_sto, precio, precioPro)
    case 0:
        print("Chao")
    case _:
        print("Esa opción no existe")