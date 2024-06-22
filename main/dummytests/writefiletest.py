# write test

text = input("Type anything here: ")
if text != "":
    create =open('textfile.txt', "w")
    create.write(text)
    create.close()
else:
    print("No input")
