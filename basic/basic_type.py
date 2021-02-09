intero = 1
stringa = "Hello"
set1 = {"apple", "banana", "cherry", "apple", "apple"}
vero = False
dizionario = {'john': 18, 'mary': 67}

# Che tipo sono? Perche'?
type(intero)
type(stringa)
type(set1)
type(vero)
# Come testo il tipo? Perche'?
isinstance(intero, str)
isinstance(intero, dict)
isinstance(intero, list)
isinstance(intero, int)
isinstance(vero, bool)
isinstance([], (tuple, list, set))
isinstance(set1, list)
isinstance(dizionario, dict)

print("is a dict ? " + str(isinstance(dizionario,dict)))