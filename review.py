data = []
count = 0

with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print("There are a total of", len(data), "lines.")

# print(len(data))
# print(data[0])
# print("-----------------")
# print(data[1])

sumLength = 0
for d in data:
    sumLength += len(d)
print("The average is", sumLength / len(data))