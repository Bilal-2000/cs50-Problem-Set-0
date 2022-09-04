emoji = {
    ":)": "😀",
    ":(": "🙁"
}


def convert(str):
    temp = str.split()
    for index in temp:
        if index in emoji:
            str = str.replace(index, emoji.get(index))
    return str


def main():
    # Hello :)
    str = input("Please input a string?\n")
    print((convert(str)))


main()
