#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    no = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            no += 1
        except IndexError:
            raise IndexError
        except:
            pass
    print()
    return no
