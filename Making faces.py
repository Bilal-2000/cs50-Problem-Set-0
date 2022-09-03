emoji = {
    ":)": "😀",
    ":(": "🙁"
}


def convert(str):
    temp = ""
    for index in range(len(str)):
        if ":)" in str:
            temp = temp + str.replace(":)", emoji.get(":)"))
            break
        elif ":(" in str:
            temp = temp + str.replace(":(", emoji.get(":("))
            break
        else:
            temp += str
    return temp


def main():
    # Hello :)
    str = input("Please input a string?\n")
    print(convert(str))


main()
