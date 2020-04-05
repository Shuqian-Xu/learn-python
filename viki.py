
def read_file(filename):
    lines = []
    with open(filename, "r", encoding="utf-8-sig") as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_image_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(" ")
        name = s[1]
        if name == "Allen":
            if s[2] == "貼圖":
                allen_sticker_count += 1
            elif s[2] == "圖片":
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == "Viki":
            if s[2] == "貼圖":
                viki_sticker_count += 1
            elif s[2] == "圖片":
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print("Allen has said", allen_word_count, "words.")
    print("Viki has said", viki_word_count, "words.")
    print("Allen has given", allen_sticker_count, "stickers.")
    print("Viki has given", viki_sticker_count, "stickers,")
    print("Allen has given", allen_image_count, "images.")
    print("Viki has given", viki_image_count, "images.")

def main():
    lines = read_file("[LINE]Viki.txt")
    convert(lines)

main()