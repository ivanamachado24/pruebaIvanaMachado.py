#gestion de inventario

#list to store the products
product_inventory= []
#function to add products
def add_products():
    for i in range(5):
        Name = input ("ingresa el nombre del producto (o escribe 'salir' para terminar): ").strip ()
        if Name.lower()== "salir":
            break

        #Request price and validate
        price = input("jngresa el precio del producto: ")
        try :
            price = float (price)
        except ValueError:
            print("el numero debe de ser valido,intentalo nuevamente")
            continue

        #Request the quantity of products and validate
        quantity =input("ingrese la cantidad de productos:")
        try:
            quantity = int (quantity)
        except ValueError:
            print("la cantidad debe ser en numeros enteros ,intentelo nuevamente")
            continue

        #dictionary for the product
        products = {
            "Name":Name,
            "price": price,
            "quantity": quantity
            }
        
        #add product to inventory list
        product_inventory.append(products)
        print (f"produto '{Name}'añadido correctamente")

        if price > 0 and quantity >= 0:
            print ("producto agregado.\n")
        else :
            print("precio y cantidad deben ser numeros positivos")

#function to search for the product
def searchProducts():
    Name = input("Ingresa el nombre del producto que deseas buscar: ").strip()
    found_proudcts = [products for products in product_inventory if products["Name"].lower() == Name.lower()]

    if not found_proudcts:
        print(f"No se encontró el producto '{Name}'.")
    else:
        for products in found_proudcts:
            print(f"Producto encontrado:")
            print(f"Nombre: {products['Name']}")
            print(f"Precio: ${products['price']}")
            print(f"Cantidad: {products['quantity']}")

#function to update the price of a product
def updatePrice():
    Name = input ("ingresa el nombre del producto del cual quieres cambiarle el precio: ").strip()
    found_products = [products for products in product_inventory if products ["Name"].lower()==Name.lower()]
    if not found_products:
        print(f"No se encontró el producto '{Name}'.")
    else:
        for products in found_products:
            print(f"Producto encontrado: {products['Name']} con precio actual ${products['price']}")
        new_price = input("Ingresa el nuevo precio: ")
        try:
            for products in found_products:
                products["precio"] = new_price
            print("Precio actualizado correctamente.")
        except ValueError:
            print("El precio ingresado no es válido. No se actualizó el precio.")

#function to delete product
def delete_product():
    Name = input("Ingresa el nombre del producto que deseas eliminar: ").strip()
    encontrados = [product for product in product_inventory if product["Name"].lower() == Name.lower()]
    
    if not encontrados:
        print(f"No existe el producto'{Name}'.")
    else:
        for producto in encontrados:
            product_inventory.remove(producto)
        print(f"Producto '{Name}' eliminado.")

#function to calculate the total value
def calculateTotalValue():
    if not product_inventory:
        print ("no hay productos registrados")
        return
    total = sum(map(lambda product: product["price"] * product["quantity"], product_inventory))
    print(f"El valor total de la compra es: ${total:.2f}")

#main menu
def menu():
    while True:
        print("\n--- Menú para gestión de inventario ---")
        print("1. añade los 5 productos")
        print("2. Buscar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            add_products()
        elif opcion == "2":
            searchProducts()
        elif opcion == "3":
            updatePrice()
        elif opcion == "4":
            delete_product()
        elif opcion == "5":
            calculateTotalValue()
        elif opcion == "6":
            print("¡adios!")
            break
        else:
            print("Opción no válida, por favor elige una opción del 1 al 6.")

# Ejecuta el menú
menu()