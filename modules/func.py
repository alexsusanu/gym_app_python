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
