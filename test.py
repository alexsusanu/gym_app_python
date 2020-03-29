def delete():
    print("member deleted")

def insert():
    print("Member added")

def select(arg):
    switch = {
        1: insert,
        2: delete,
    }
    switch.get(arg, "invalid")()

select(2)
