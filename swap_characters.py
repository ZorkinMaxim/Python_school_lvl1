word = 'abcdefgh'

ia = int(input('Enter first index:'))
ib = int(input('Enter second index:'))

if ia < ib:
    s1 = word[:ia]
    s2 = word[ia+1:ib]
    s3 = word[ib+1:]
    print('testing segments:', s1, s2, s3)
    swapped_word = s1 + word[ib] + s2 + word[ia] + s3
    print(swapped_word)
elif ia > ib:
    s1 = word[:ib]
    s2 = word[ib + 1:ia]
    s3 = word[ia + 1:]
    print('testing segments:', s1, s2, s3)
    swapped_word = s1 + word[ia] + s2 + word[ib] + s3
    print(swapped_word)
else:
    input('Wrong index! Do you wont to try again? y/n :')
    if 'y':
        ia = int(input('Enter first index:'))
        ib = int(input('Enter second index:'))
        if ia < ib:
            s1 = word[:ia]
            s2 = word[ia + 1:ib]
            s3 = word[ib + 1:]
            print('testing segments:', s1, s2, s3)
            swapped_word = s1 + word[ib] + s2 + word[ia] + s3
            print(swapped_word)
        elif ia > ib:
            s1 = word[:ib]
            s2 = word[ib + 1:ia]
            s3 = word[ia + 1:]
            print('testing segments:', s1, s2, s3)
            swapped_word = s1 + word[ia] + s2 + word[ib] + s3
            print(swapped_word)
        else:
            pass

