emoji = {
    ":)": "😀",
    ":(": "🙁"
}


def convert(str):
    if ":)" in str:
        str = str.replace(":)", emoji.get(":)"))
    elif ":(" in str:
        str = str.replace(":(", emoji.get(":("))
    return str


def main():
    # Hello :)
    str = input("Please input a string?\n")
    print(convert(str))


main()
