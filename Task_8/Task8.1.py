# Создать информационную систему позволяющую работать с сотрудниками
# некой компании \ студентами вуза \ учениками школы
# '''

database = {}
d_b = {
    "parents": 1,
    "children": 2,
    "title": 3,
    "stand": 4,
}


def reading_file_to_dict(number_file):
    with open(f"{number_file}.txt", "r", encoding="utf-8") as file_1:
        data = [i.split("\n")[0] for i in file_1.readlines()]
        # print(data)
        database[number_file] = []
        for i in data:
            database[number_file].append(tuple(i.split(";")))


def print_children(second_name):
    id = [i[0] for i in database[1] if second_name in i][0]
    deti = [i for i in database[2] if id == i[0]]
    print(*[" ".join(i[1:4]) + "\n" for i in deti])


def print_post(second_name):
    id = [i[0] for i in database[1] if second_name in i][0]
    f_title = [i for i in database[3] if id == i[0]]
    print(*[" ".join(i[1:3]) + "\n" for i in f_title])


def print_standing(second_name):
    id = [i[0] for i in database[1] if second_name in i][0]
    f_title = [i for i in database[4] if id == i[0]]
    print(*[" ".join(i[1:2]) + "\n" for i in f_title])


def search_base():
    # global number_file
    number_file = int(
        input("Вывести по фамилии  Детей - 1 ; Должность - 2 ; Стаж - 3 ")
    )
    if number_file == 1:
        surname = input("Введите фамилию -> ")
        reading_file_to_dict(number_file)
        number_file = 2
        reading_file_to_dict(number_file)
        print_children(surname)
    elif number_file == 2:
        surname = input("Введите фамилию -> ")
        reading_file_to_dict(number_file - 1)
        reading_file_to_dict(number_file + 1)
        print_post(surname)
    elif number_file == 3:
        surname = input("Введите фамилию -> ")
        reading_file_to_dict(number_file - 2)
        reading_file_to_dict(number_file + 1)
        print_standing(surname)


search_base()
