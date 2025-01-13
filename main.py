from design.products import desing , tableProducts, addProduct, tableProductsBycategory
from logic.products import updateInventoryBycode

def main():
    match desing():  
        case 1:
            addProduct()  
        case 2:
            tableProducts()
        case 3:
            tableProductsBycategory(input("Ingrese la Categoria ejemplo (panes,pasteles,postres): "))
        case 0:
            print("Gracias por utilizar el sistema")
        case _: 
            print("Esta opción no existe")


main()