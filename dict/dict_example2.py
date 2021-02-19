# Method that takes a dict (agenda) and a string (user)
# Check inside the agenda is the user exists
def find_user(agenda, user):
    if user in agenda:
        return True
    else:
        return False

# This method check if the user exists and later if the key user the street exist
# The dict is a nested structure
def get_address(agenda, user):
    if user in agenda:
        if 'street' in agenda[user]:
            return agenda[user]['street']
        else:
            None
    else:
        None


# This method shows how to build a dict
# Empty dict and adding an element
# dict_1 = {}
# dict_1['john'] = value
def create_dictionary():
    user1_address = {'street': 'Elmield', 'cap': 'cb4'}
    user1_detail = {'nazionalita': 'Italiana', 'eta': 18, 'street': user1_address}
    user2 = {'nazionalita': 'Italiana', 'eta': 17, 'indirizzo': {'street': 'Oxford', 'cap': 'ox1'}}
    agenda = {'John': user1_detail, 'Sophia': user2}

    user3 = {'nazionalita': ['Italiana', 'British'], 'eta': 0, 'indirizzo': {'street': 'Cornovaglia', 'cap': 'CW1'}}
    agenda["Ben"] = user3

    user4 = {'eta': 19, 'indirizzo': {'street': 'Cornovaglia', 'cap': 'CW1'}}
    agenda["Irin"] = user4
    user5 = {}
    agenda["Falco"] = user5
    return agenda

def main():
    new_agenda = create_dictionary()
    user_to_find = input("Enter name to search in the agenda: ")
    print("Given " + user_to_find)
    result = find_user(new_agenda, user_to_find)
    if result:
        print("Found " + user_to_find)
    else:
        print("Not Found " + user_to_find)
    address_res = get_address(new_agenda, user_to_find)
    if address_res != None:
        print("Address: "+ str(address_res))
    else:
        print("Address not available")

if __name__ == "__main__":
    main()