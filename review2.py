data = []
count = 0

with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print("There are a total of", len(data), "lines.")

word_count = {}
for d in data:
    words = d.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

while True:
    word = input("What word do you want to look for: ")
    if word == "q":
        break
    if word in word_count:
        print(word_count[word])
    else:
        print("The word doesn't exist.")