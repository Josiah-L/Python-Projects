def main():
    try:
        num = int(input("Enter a number: "))

        while num > 1:
            num = collatz(num)
            print(num)

    except ValueError:
        print("Invalid Number. Please enter a numerical character.")
        print()
        main()



def collatz(num):
    rem = num % 2

    if rem == 0:
        num = num // 2
    elif rem == 1:
        num = (3 * num) + 1
    return num


main()