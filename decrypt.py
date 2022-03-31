
key = input("Key : ")
word = input("Word : ")

if len(key) != len(word):
    print("answer is Wrong")
    exit()

key_list = [i for i in key]
word_list = [i for i in word]

size_value = len(key_list)

for i in range(size_value-1, -1, -1):
    if word_list[i] in word_list:
        key_list.remove(word_list[i])
        word_list.remove(word_list[i])
        # print(word_list)
        # print(key_list)

# print(word_list)
# print(key_list)
if len(key_list) == 0 and len(word_list) == 0:
    print("the answer is Right")
else: 
    print("Wrong")