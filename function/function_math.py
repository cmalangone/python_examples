def multiple(number1, number2):
    tot = number1 * number2
    return tot

def sum(a, b):
    tot = a + b
    return tot

def main():
    # Fase di input e definizioni varibiabili
    numero1input = input("Enter first number: ")
    numero2input = input("Enter second number: ")
    print("Given " + numero1input + ", " + numero2input)
    # Gli input sono string per sicurezza converto!
    numero1=int(numero1input)
    numero2=int(numero2input)
    # chiamo le mie operazioni
    tot_sum = sum(numero1, numero2)
    tot_mul = multiple(number1=numero2,number2=numero1)
    print("Sum: " + str(tot_sum))
    print("Multiple:" + str(tot_mul))

if __name__ == "__main__":
    main()
