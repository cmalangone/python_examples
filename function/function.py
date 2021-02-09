# This example explain just simple method declaration
def multiple():
    alpha = 1.1
    beta = 2
    tot = alpha * beta
    print("Multiply: " + str(tot))

def sum():
    number_1 = 4
    number_2 = 3
    tot = number_1 + number_2
    print("Sum = " + str(tot))

def main():
    # chiamo le mie operazioni
    sum()
    multiple()

if __name__ == "__main__":
    main()