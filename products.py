products = []
while True:
    name = input("Please input the name of the good: ")
    if name == "q":
        break
    price = input("Please input the price of the good: ")
    # p = [name, price]
    # # p = []
    # # p.append(name)
    # # p.append(price)
    # products.append(p)
    products.append([name, price])
print(products)

for product in products:
    print(product[0])