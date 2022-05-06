import pathlib
#
# words = [
#     {'english': 'apple', 'persion': 'sib'},
#     {'english': 'tree', 'persion': 'derakht'},
#     {'english': 'i', 'persion': 'man'},
#
# ]
list_en_per = []
list_temp_en_per = []
list_temp_per_en = []
words = []
list_dic = []


def get_words():
    get_word = input("Please Inter words:")
    get_word = get_word.lower()
    return get_word


def menu_def():
    list_en_per = []
    # list_temp_en_per = []
    flag_en_per = True
    flag_per_en = True
    str_en = ""
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
        for i in range(len(list_en_per)):
            for j in range(len(words)):
                if list_en_per[i] == words[j]["english"]:
                    list_temp_en_per.append(words[j]["persion"])
                    flag_en_per = False # barrasi vojode mani kalame dar farhang loghat
            if flag_en_per: # agar mani kalame dar farhang loghat vojod nadasht khodash ra chap konad
                list_temp_en_per.append(list_en_per[i])
            if "." in list_en_per[i]:
                list_temp_en_per.append("\n")

            flag_en_per = True

        for i in range(len(list_temp_en_per)):
            if i == "\n":
                print()
            str_en += f"{list_temp_en_per[i]} "
        print(str_en)

        list_en_per.clear()
        list_temp_en_per.clear()

    if get_chooice == 3:
        list_per_en = get_words().replace('.', ' \n')
        list_per_en = list_per_en.split(" ")
        # print(list_per_en)
        for i in range(len(list_per_en)):
            for j in range(len(words)):
                if list_per_en[i] == words[j]["persion"]:
                    list_temp_per_en.append(words[j]["english"])
                    flag_per_en = False
            if flag_per_en:
                list_temp_per_en.append(list_per_en[i])
            if "." in list_per_en[i]:
                list_temp_per_en.append("\n")

            flag_per_en = True

        for i in range(len(list_temp_per_en)):
            if i == "\n":
                print()
            str_per += f"{list_temp_per_en[i]} "
        print(str_per)
        list_temp_per_en.clear()

    if get_chooice == 4:
        f = open('dic.txt', 'w')
        str_en = repr(words)
        f.write(str_en)
        f.close()
        exit()


def load_db():
    f = open('dic.txt', 'r')
    text = f.readlines()
    for line in text:
        line = line.replace("[", '')
        line = line.replace("english", '')
        line = line.replace("persion", '')
        line = line.replace("\n", '')
        line = line.replace("]", ',')
        line = line.replace("}", '')
        line = line.replace("{", '')
        line = line.replace('"', '')
        line = line.replace("'", '')
        line = line.replace(':', '')
        line = line.replace(' ', '')
        list_dic = line.split(",")
    f.close()
    words = create_dic(list_dic)
    return words


def create_dic(list_dic):
    h = 0
    for i in range(len(list_dic) - 1):
        if h < len(list_dic)-1:
            words.append({'english': list_dic[h], 'persion': list_dic[h + 1]})
            h += 2
    return words

if pathlib.Path('dic.txt').exists():
        load_db()
else:
    print("Not Found File")
while True:
    menu_def()