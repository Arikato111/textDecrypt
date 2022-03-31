import random
import hashlib

# value_input = input()
# key_endcrypt = hashlib.md5(value_input.encode('utf-8')).hexdigest()
# print(key_endcrypt)

# text = input("Text : ")
# ascii_values = []
# for character in text:
#     ascii_values.append(ord(character))
#     print(ord(character), end='')

while True:
    word = input("Your answer :")
    decrypt = input("crypt value : ")
    if len(word) == len(decrypt):
        break
    print("size !=")

print("len of your word : ", len(word))
print("")

while True:
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
    if only_one_text == decrypt:
        print("Right!! word is :", word)
        break
