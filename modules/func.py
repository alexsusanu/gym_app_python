""" mix function to avoid repetion """

import re

def quit_or_menu(user_input):
    """ quit or main menu """
    quit_arr = ('q', 'Q', 'Quit', 'quit', 'QUIT')
    #m = Menu()  #to redo menu func in menu file first

    if user_input in quit_arr:
        exit()
    elif user_input == 'm':
        #Menu()
        pass
    #else:
    #    print("Invalid input. Retry: ", end=" ")
    #    quit_or_menu(user_input = input())

def print_stars():
    """ take me to the stars """
    print(20 * "*")

def check_input(user_input, array):
    """ check user input is what is expected """
    while True:
        if int(user_input) not in array:
            print("Invalid input. Retry")
            user_input = input()
            continue
        else: return user_input

#desc => description, use as keys in dict
#arr => members list from sql
def send_to_dict(arr, desc):
    """ array/list to dictionary """
    to_dict = dict()
    count = 0
    for index in arr:
        to_dict[count] = {}
        for i, element in enumerate(desc):
            #print("%s: %s" % (desc[i], index[i]))
            to_dict[count][element] = index[i]
        count += 1
    return to_dict

def from_dict_by_id(dictionary, by_id):
    """ retrieve from dictionary by key/id """
    for index in dictionary:
        if int(by_id) in dictionary[index].values():
            for key, value in dictionary[index].items():
                print("%s: %s" % (key, value))
        print_stars()
    #return dictionary[index]['FIRST_NAME'], dictionary[index]['LAST_NAME']

def check_alpha(user_input):
    """ check name typed is alpha """
    while True:
        if user_input.isalpha():
            return user_input.title()
        else:
            print("Letters only. q to quit or m for menu")
            print("Try again: ", end=" ")
            user_input = input()
            quit_or_menu(user_input)

def check_digit(user_input):
    """ check is digit only """
    while True:
        if user_input.isdigit():
            return user_input
        else:
            print("Digits only. q to quit or m for menu")
            print("Try again: ", end=" ")
            user_input = input()
            quit_or_menu(user_input)

def check_email(user_input):
    """ regex check email format """
    """ note the 'space' after '\t' for spaces"""
    while True:
        if not re.fullmatch(r"[^@\t ]+@[^@\t ]+\.[^@\t ]+", user_input):
            print("Not a valid format. q to quit, m for mai menu")
            print("Retry: ", end=" ")
            user_input = input()
            quit_or_menu(user_input)
        else:
            return user_input

def yes_no(answer):
    """ y|n to quit """
    arr_y = ['yes', 'y']
    arr_n = ['no', 'n']
 
    while True:
        if answer.lower() in arr_y:
            return True
        elif answer.lower() in arr_n:
            return False
        else:
            print("y|n answer. Retry: ", end=" ")
            answer = input()
