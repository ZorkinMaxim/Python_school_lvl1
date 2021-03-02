sms = input("enter sms text:")

a = "abcdefghijklmnopqrstuvwxyz"
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = "0123456789!., "
#allowed_characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
# 'v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U',
# 'V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0',',','!',' ','.']

# N1
for index in range(len(sms)):
    if sms[index] not in a and sms[index] not in A and sms[index] not in n:
        print("You have used the forbidden symbol!")
        break
    elif len(sms) >= 20:
        print("EROR!!! sms too long (", len(sms), "characters )")
        break
    elif index == len(sms)-1:
        print("Your original sms:", sms)
#else:
#    print("Your original sms:", sms)


# N2
#if any(x not in allowed_characters for x in sms):
#    print("You have used the forbidden symbol!")
#else: print("Your original sms:", sms)


# №3 Only letters
#for index in range(len(sms)):
#    if str.isalpha(sms):
#        print("sms", sms, end ="")
#        break
#    else:
#        print("False")
#        break





#for x in sms:
#    if x not in allowed_characters:
#        print("You have used the forbidden symbol!")
#        break
#else:
#    print("Your original sms:", sms)




    #else:
    #    print("You have used the forbidden symbol!")
    #    break

#if len(sms) <= 20:
#    print("Your original sms:", sms)
#else:
#    print("EROR!!! sms too long (", len(sms), "characters )")


#string.ascii_lowercase, string.ascii_uppercase, "0123456789!.,"
#if len(sms) <= 20:
#    print("Your original sms:", sms)
#elif len(sms) >= 20:
#    print("EROR!!! sms too long (", len(sms), "characters )")
#else:
















