import random

print("Magic 8-ball Started Enter 'quit' to quit")

while True:

    x = input("Ask a Question : ")

    if x != 'quit':

        prediction = ["Yes","No","Maybe","Maybe Not","Dont Know?","Yesn't"]

        ListToConvert = random.choices(prediction)

        EmptyStr = ""

        ListToStr = EmptyStr.join(ListToConvert)

        print(ListToStr)

    else:
        break
