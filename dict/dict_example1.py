# Method that takes a dict (agenda) and a string (user)
# Check inside the agenda is the user exists
def find_user(agenda, user):
    if user in agenda:
        return True
    else:
        return False

# This method shows how to build a dict
# Empty dict and adding an element
# dict_1 = {}
# dict_1['john'] = value
def create_dictionary():
    user1_address = {'street': 'Elmield', 'cap': 'cb4'}
    user1_detail = {'nazionalita': 'Italiana', 'eta': 18, 'indirizzo': user1_address}
    user2 = {'nazionalita': 'Italiana', 'eta': 17, 'indirizzo': {'street': 'Oxford', 'cap': 'ox1'}}
    agenda = {'John': user1_detail, 'Lorena': user2}

    user3 = {'nazionalita': ['Italiana', 'British'], 'eta': 0, 'indirizzo': {'street': 'Cornovaglia', 'cap': 'CW1'}}
    agenda["Ben"] = user3

    user4 = {'eta': 19, 'indirizzo': {'street': 'Cornovaglia', 'cap': 'CW1'}}
    agenda["Irin"] = user4

    return agenda

# Main
def main():
    new_agenda = create_dictionary()
    user_to_find = input("Enter name to search in the agenda: ")
    print("Given " + user_to_find)
    result = find_user(new_agenda, user_to_find)
    if result:
        print("Found " + user_to_find)
    else:
        print("Not Found " + user_to_find)

if __name__ == "__main__":
    main()