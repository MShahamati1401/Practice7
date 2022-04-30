import pathlib
#
# words = [
#     {'english': 'apple', 'persion': 'sib'},
#     {'english': 'tree', 'persion': 'derakht'},
#     {'english': 'i', 'persion': 'man'},
#
# ]
list_temp_en_per = []
list_temp_per_en = []


def get_words():
    get_word = input("Please Inter words:")
    get_word = get_word.lower()
    # get_word = get_word.replace("\n", " ")
    # get_word = get_word.replace("\n", " ")
    return get_word


def menu_def():
    flag_en_per = True
    flag_per_en = True
    str = ""
    str_per = ""
    print("1- add new word")
    print("2- translation english to persion")
    print("3- translation persion to english")
    print("4- exit")
    get_chooice = int(input("Please Choice Number: "))
    if get_chooice == 1:
        get_english = input("Please Inter word English:")
        get_persion = input("Please Inter word Persion: ")
        words.append({'english': get_english, 'persion': get_persion})
        print(words)

    if get_chooice == 2:
        list_en_per = get_words().replace('.', ' \n')
        list_en_per = list_en_per.split(" ")
        print(list_en_per)
        for i in range(len(list_en_per)):
            for j in range(len(words)):
                if list_en_per[i] == words[j]["english"]:
                    list_temp_en_per.append(words[j]["persion"])
                    flag_en_per = False
            if flag_en_per:
                list_temp_en_per.append(list_en_per[i])
            if "." in list_en_per[i]:
                list_temp_en_per.append("\n")
                print("Yes")
            else:
                print("No")
            flag_en_per = True

        for i in range(len(list_temp_en_per)):
            if i == "\n":
                print()
            str +=f"{list_temp_en_per[i]} "
        print(str)
        list_temp_en_per.clear()

    if get_chooice == 3:
        list_per_en = get_words().replace('.', ' \n')
        list_per_en = list_per_en.split(" ")
        print(list_per_en)
        for i in range(len(list_per_en)):
            for j in range(len(words)):
                if list_per_en[i] == words[j]["persion"]:
                    list_temp_per_en.append(words[j]["english"])
                    flag_per_en = False
            if flag_per_en:
                list_temp_per_en.append(list_per_en[i])
            if "." in list_per_en[i]:
                list_temp_per_en.append("\n")
                print("Yes")
            else:
                print("No")
            flag_per_en = True

        for i in range(len(list_temp_per_en)):
            if i == "\n":
                print()
            str_per += f"{list_temp_per_en[i]} "
        print(str_per)
        list_temp_per_en.clear()

    if get_chooice == 4:
        f = open('dic.txt', 'w')
        str = repr(words)
        f.write(str)
        f.close()
        exit()
def load_db():
    f = open('dic.txt', 'r')
    text = f.read()
    print(text)
    # for line in text:
    #     line = line.replace("[", '')
    #     # line = line.replace("\n", '')
    #     line = line.replace("]", ',')
    #     line = line.replace("}", '')
    #     line = line.replace("{", '')
    #     line = line.replace('"', '')
    #     # line = line.replace("'", '')
    #     # line = line.replace(':', ' = ')
    #     # line = line.replace(' ', '')
    #     list_faktor = line.split("}")
    f.close()
    # print(list_faktor)
    print(type(text))
    # print(text[0]["english"])
    return text


while True:
    if pathlib.Path('dic.txt').exists():
        words = load_db()
        menu_def()
    else:
        print("Not Found File")