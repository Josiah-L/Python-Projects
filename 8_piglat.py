# English to Pig Latin
print('Enter the English message to translate into Pig Latin:')
message = input()

vowels = ('a','e','i','o','u','y')

piglaitn = []
for word in message.split():
    prefix = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix += word[0]
        word = word[1:]
    if len(word) == 0:
        continue

    suffix = ''
    while not word[-1].isalpha():
        suffix += word[-1]
        word = word[:-1]

    wasUpper = word.isupper()
    wasTitle = word.istitle()
    
    word = word.lower()

    prefixCon = ''
    while len(word) > 0 and not word[0] in vowels:
        prefixCon += word[0]
        word = word[1:]

    if prefixCon != '':
        word += prefixCon + 'ay'
    else:
        word += 'yay'

    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    piglaitn.append(prefix + word + suffix)
print(' '.join(piglaitn))
