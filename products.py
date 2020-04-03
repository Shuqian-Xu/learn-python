import os

def read_file(fileName, products):
    with open(fileName, "r", encoding="utf-8") as f:
        for line in f:
            if "Good,Price" in line:
                continue
            name, price = line.strip().split(",")
            products.append([name, price])
    return products

def user_input(products):
    while True:
        name = input("Please input the name of the good: ")
        if name == "q":
            break
        price = input("Please input the price of the good: ")
        products.append([name, price])
    print(products)
    return products

def print_products(products):
    for product in products:
        print(product[0], "has the price of", product[1])

def write_file(fileName, products):
    with open(fileName, "w", encoding="utf-8") as f:
        f.write("Good,Price\n")
        for p in products:
            f.write(p[0] + "," + p[1] + "\n")

def main():
    fileName = "products.csv"
    products = []
    if os.path.isfile(fileName):
        products = read_file(fileName, products)
    products = user_input(products)
    print_products(products)
    write_file("products.csv", products)

main()