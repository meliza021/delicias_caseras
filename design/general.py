from design.products import  tableProducts, tableProductsByCategory, tableProductsByCode, tableProductsByName, newProduct, obtener_opcion
from design.general import *
from logic.products import updateInventoryByCode
from design.customer import *
from design.order import *
from logic.order import *
from  design.order import desingedit

def menu(): #Menu principal
    print("""
          *************************************************************************
                                Bienvenido al menú principal
             Registrar pedidos   |   Productos   |   Editar pedidos   |   Salir      
                     1           |       2       |         3          |     0
          *************************************************************************
            """)
    principal = input("Ingrese el número de la opción: ")
    match principal:
        case "1":
            while True:
                option = designClient()
                match option:
                    case "1":
                        formularyTakeOrder()
                    case "2":
                        seeOrders()
                    case "0":
                        return menu()  
                    case _:
                        input("El valor ingresado no existe, presione enter para continuar: ")
                        return menu()
        case "2":
            while True:
                option = obtener_opcion()
                match option:
                    case 1:
                        tableProducts()
                    case 2:
                        tableProductsByCategory(input("Ingrese la categoria. Ejemplo ('pan', 'pastel', 'postre'): ").lower())
                    case 3:
                        tableProductsByCode(input("Ingrese el codigo del producto: "))
                    case 4:
                        tableProductsByName(input("Ingrese el nombre del producto: "))
                    case 5:
                        updateInventoryByCode(input("Ingrese el codigo del producto: "))
                    case 6:
                        newProduct() 
                    case 0:

                        return menu()
                    case _:
                        input("El valor ingresado no existe, presione enter para continuar: ")
                        return menu()
        case "3":
            while True:
                option = desingedit()
                match option:
                    case 1:
                        editOrder(int(input("Ingrese el codigo del pedido: ")))
                    case 2:
                        deleteJSON(int(input("Ingrese el codigo del pedido: ")))
                    case 0:
                        return menu()
                    case _:
                        input("El valor ingresado no existe, presione enter para continuar: ")
                        return menu()