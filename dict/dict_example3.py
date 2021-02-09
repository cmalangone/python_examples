# Calculate the average of the age.
# You must check if eta exist. Dict doesn't have a schema!
def calculate_avg_age(agenda):
    tot_eta = 0
    for user in agenda.keys():
        # debug here if you need
        # print(agenda[user]
        if 'eta' in agenda[user]:
            tot_eta = tot_eta + agenda[user]['eta']

    return tot_eta

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
    user5 = {}
    agenda["Falco"] = user5
    return agenda

def main():
    new_agenda = create_dictionary()
    average_age = calculate_avg_age(new_agenda)
    print("Average age: " + str(average_age))

if __name__ == "__main__":
    main()