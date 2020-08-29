import random, sys

def main():
    alist = ['coins', 'umbrella handle', 'pencils', 'pens', 'hockey stick handle',
        'vibrators', 'small pp']

    # Reorganizing the list
    holder = alist[1]
    alist[1] = alist[5]
    del alist[5]
    alist.append(holder)

    # First list
    ordered(alist)

    # Reordering
    while True:
        reorder(alist)



def reorder(alist):
    print()
    print("Do you want to shake things up? (y/n)")
    check = input()
    print()

    # Checks if yes or no
    if check == 'y':
        random.shuffle(alist)
        ordered(alist)
    elif check == 'n':
        print("Alright, have a good day.")
        sys.exit()
    else:
        print("Incorrect input.")


def ordered(alist):
    # The actual ordered list
    print("Things that I've shoved up my... you get the rest...")
    for i, it in enumerate(alist):
        print(i+1, end='. ')
        print(it)


main()