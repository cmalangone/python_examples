# concetto di variabile
nome = "cinzia"
print("ciao" + nome)

# Tipi di data e strutture dati.
stringa = "Benjamin"
intero = 1
doppio = 1.1
vero = True

# Collection
lista = [1, 3, 2]
lista2 = [1, "a", 1.1]  # mutable e duplicati!
tupla1 = (1, 3, 4)  # immutable!!!!
set1 = {"apple", "banana", "cherry", "apple", "apple"}  # unici elementi e immutabible
hash1 = {'1': 'cinzia', '4': 'sophia', '7': 'ben'}

print(intero)
print(doppio)
print(lista)
print(lista2)
print(tupla1)
print(hash1)
print(set1)

# Collection di tutte le strutture! Nested structure.


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

print(lista[0])
# print(hash1[0])
print(hash1['7'])
print(hash1)  # Prints complete dictionary
print(hash1.keys())  # Prints all the keys
print(hash1.values())  # Prints all the values

if '8' in hash1:
    print(hash1['8'])
else:
    print("8 non trovato")

if '9' in hash1:
    print(hash1['9'])
else:
    print("9 non trovato")

# loop list
a = ["italia", "uk"]
for elem in a:
    print(elem)

# loop hash - exploding using variable to explain what is going on
hashVar = {'cinzia': 'Malas', 'sophia': 'Relon'}
chiavi = hashVar.keys()
for chiave in chiavi:
    print(chiave)
    print(hashVar[chiave])
    print(chiave + " " + hashVar[chiave])

# premessa:
# while fa un test sulla condizione del ciclo vero.
# Esce dal ciclo quando il test e' falso
# mentre (1 < 2) esegui
lista = [1, 2, 4, 5, 7, 4]
indice = 0
while (indice < len(lista)):
    print("True")
    print(lista[indice])
    indice = indice + 1

print("False")
