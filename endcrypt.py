import random
import hashlib
from turtle import pos

word = input("Word :")
time_loop = int(input("Len of Ecy : "))

print("len of your word : ", len(word))
print("")

for elifaj in range(time_loop):
    endcrypt_word = {}
    his_num = []
    for i in range(0, len(word)):
        position_ran = ""
        while True:
            position_ran = random.randrange(0, len(word))
            if position_ran in his_num:
                continue

            his_num.append(position_ran)
            endcrypt_word.update({position_ran: word[i]})
            break
    only_one_text = ""
    for i in range(len(endcrypt_word)):
        print(endcrypt_word[i], end='')
        only_one_text += endcrypt_word[i]
    print("")
print("")
