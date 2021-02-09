def find_user(agenda, user):
    if user in agenda:
        return True
    else:
        return False

def get_address(agenda, user):
    if user in agenda:
        if 'street' in agenda[user]:
            return agenda[user]['street']
        else:
            None
    else:
        None

def calculate_avg_age(agenda):
    tot_eta = 0
    for user in agenda.keys():
        # debug here if you need
        # print(agenda[user]
        if 'eta' in agenda[user]:
            tot_eta = tot_eta + agenda[user]['eta']

    return tot_eta

def create_dictionary():
    user1_address = {'street': 'Elmield', 'cap': 'cb4'}
    user1_detail = {'nazionalita': 'Italiana', 'eta': 18, 'street': user1_address}
    user2 = {'nazionalita': 'Italiana', 'eta': 17, 'indirizzo': {'street': 'Oxford', 'cap': 'ox1'}}
    agenda = {'John': user1_detail, 'Lorena': user2}

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
        print("Address: "+ address_res)
    else:
        print("Address not available")

if __name__ == "__main__":
    main()