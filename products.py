products = []
while True:
    name = input("Please input the name of the good: ")
    if name == "q":
        break
    price = input("Please input the price of the good: ")
    products.append([name, price])
print(products)

for product in products:
    print(product[0], "has the price of", product[1])

with open("products.csv", "w", encoding="utf-8") as f:
    f.write("Good,Price\n")
    for p in products:
        f.write(p[0] + "," + p[1] + "\n")