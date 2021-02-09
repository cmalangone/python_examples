
def main():
    piove = False
    # se non c'e' per lui e' true!
    if piove == True:
        print("sta piova")
    else:
        print("non sta piove")

    # another example
    number = 1
    if number > 1:
        print("number is higher than 1")

    # Example with string
    nome = "John"
    eta = 17
    if nome == "John":
        if eta >= 18:
            print("John is an adult")
        else:
            print("John is not an adult")
    else:
        print("It is not John")

if __name__ == "__main__":
    main()