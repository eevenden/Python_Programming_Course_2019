#Author: Emily Evenden
#Final Lab
#Date: 10/9
#Time: 30 mins

#Here, we create dictionary of countries and the number of refugees living in them
refugees = {'Algeria': 90000, 'Bangladesh': 32355, 'Botswana': 2833, 'Burkina Faso': 20356, 'Chad': 400615}

#In this function, we print both the key and value of each entry in the dictionary
def print_list(list):
    for (key, value) in list.items():
        print key, value

print_list(refugees)

#In this function, we print only the key of each dictionary entry
def print_keys(list):
    for key in list.keys():
        print key

print_keys(refugees)

#In this function, we print only the value of each dictionary entry
def print_values(list):
    for value in list.values():
        print value

print_values(refugees)

#In this function, we print both the key and the value of each dictionary entry but also
#concatenate it to create sentences.
def print_statements(list):
    for (key, value) in list.items():
        print "There are " + str(value) + " refugees in " + str(key) + "."

print_statements(refugees)
