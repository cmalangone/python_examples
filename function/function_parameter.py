def print_name(name):
    if name == "cinzia":
        print("Hi Cinzia")
    else:
        print("Hi " + str(name)) # name could be a number ;-)

def is_snowing(is_raining, temperature):
    if is_raining == False:
        return False
    else:
        if temperature < 0:
            return True
        else:
            return False

def main():
    first_name = "John"
    raining = True
    temperature = -1
    print_name(first_name)
    result = is_snowing(raining,temperature)
    print("Is snowing?" + str(result))

if __name__ == "__main__":
    main()