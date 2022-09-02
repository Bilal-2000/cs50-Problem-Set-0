text = input("Please enter a string?\n")
temp = ""
#This is cs50
for index, val in enumerate(text):
    if val == " ":
        temp = temp + "..."
    else:
        temp = temp + val

print(temp)
