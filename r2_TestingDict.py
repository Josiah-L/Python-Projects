def main():
    print("Enter a sentence:")
    sentence = input()

    count = {}

    for char in sentence:
        count.setdefault(char, 0)
        count[char] += 1

    order(count)

def order(count):
    for k, v in count.items():
        print('[' + k + ']', end='= ')
        print(v)


main()