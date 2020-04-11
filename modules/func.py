from menu import *

def quit_or_menu(user_input):
    quit = ('q', 'Q', 'Quit', 'quit', 'QUIT')
    #m = Menu()  #to redo menu func in menu file first

    if user_input in quit:
        exit()
    elif user_input == 'm':
        #Menu()
        pass
    #else:
    #    print("Invalid input. Retry: ", end=" ")
    #    quit_or_menu(user_input = input())

def print_stars():
    print(20 * "*")

def check_input(user_input, array):
    flag = True
    while True:
        if int(user_input) not in array:
            print("Invalid input. Retry")
            user_input = input()
        else:
            return user_input
            flag = False

#desc => description, use as keys in dict
#arr => members list from sql
def send_to_dict(arr, desc):
    to_dict = dict()
    count = 0
    for index in arr:
        to_dict[count] = {}
        for i in range(0, len(desc)):
            #print("%s: %s" % (desc[i], index[i]))
            to_dict[count][desc[i]] = index[i]
        count += 1
    return to_dict

def from_dict_by_id(dictionary, by_id):
    for index in dictionary:
        if int(by_id) in dictionary[index].values():
            for key, value in dictionary[index].items():
                print("%s: %s" % (key, value))
        print_stars()
    #return dictionary[index]['FIRST_NAME'], dictionary[index]['LAST_NAME']
