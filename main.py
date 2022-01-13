import sys

products = []


def read_from_file(file_name, storage):
    f = open(file_name, "r")
    for row in f:
        storage.append(row.strip())
    f.close()
    del storage[0]


def get_memories(storage):
    memories_list = []
    for product in storage:
        products = product.split(";")
        if products[1] == "Memória":
            memories_list.append(product)
    return memories_list


# 1. Feladat
def pieces_of_products(storage, manufacturer):
    products = [product.split(";") for product in storage if product.split(";")[2].lower() == manufacturer.lower()]
    return len(products)


# 2. Feladat
def types_of_products(storage, manufacturer):
    products = {product.split(";")[1] for product in storage if product.split(";")[2].lower() == manufacturer.lower()}
    return products

# 3. Feladat
def product_list_with_price(storage, manufacturer, min=0, max=sys.maxsize):
    # a map() függvénnyel redukálom ki a nem szükséges elemeket, ami a 2, 3, 4 indexű
    products = [list(map(product.split(";").__getitem__, [2,3,4])) for product in storage if int(product.split(";")[4]) < max and int(product.split(";")[4]) > min and product.split(";")[2].lower() == manufacturer.lower()]
    return products

# Főprogram
read_from_file("Terméklista.csv", products)
memories = get_memories(products)

manufacturer = input("Kérem a gyártó nevét! :")
print(" DEMÓ : def pieces_of_products(storage, manufacturer) ".center(100, '─'))
print(f"A {manufacturer} termékeinek száma: {pieces_of_products(products, manufacturer)}")
print()
print(" DEMÓ : def types_of_prdocuts(storage, manufacturer) ".center(100, '─'))
print(f"A {manufacturer} termékfajtái: {types_of_products(products, manufacturer)}")
print()
print(" DEMÓ : def product_list_with_price(storage, manufacturer, min=0, max=sys.maxsize) ".center(100, '─'))
min_price = int(input("Adja meg az alsó határt! :"))
max_price = int(input("Adja meg a felső határt! :"))
kepernyo_lista = product_list_with_price(products, manufacturer, min_price, max_price)
print(f"{len(kepernyo_lista)} db termék esik a megadott ársávba!")
for row in kepernyo_lista:
    print(row[0].rjust(14, '_') + " : " + row[1].ljust(160, '_') + " - " + str(row[2]).rjust(10, '.') + " Ft")