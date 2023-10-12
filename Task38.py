# Задача 38  Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать
# функционал для изменения и удаления данных.
from csv import DictWriter, DictReader
from os.path import exists


def create_file():
    with open('phone.csv', 'w', encoding='UTF-8') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Телефон'])
        f_writer.writeheader()


def get_info():
    mas_info = ['Иванов', 'Иван', '84951661213']
    return mas_info


def write_file(lst):
    with open('phone.csv', 'r+', encoding='UTF-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
        with open('phone.csv', 'r+', encoding='UTF-8') as data:
            obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Телефон': lst[2]}
            res.append(obj)
            f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Телефон'])
            f_writer.writeheader()
            f_writer.writerows(res)


def read_file(filename):
    with open(filename, encoding='UTF-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
        return res


def erase_data():
    with open('phone.csv', 'r+', encoding='UTF-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
        er_data = input("Введите Имя или фамилию, которую хотите удалить: ")
        print("erdata=" + str(er_data))
        for key in res:
            print(key)
            if key['Фамилия'] == er_data:
                del key['Фамилия']
            if key['Имя'] == er_data:
                del key['Имя']
        print(res)
        with open('phone.csv', 'w', encoding='UTF-8') as file:
            new_file = DictWriter(file, fieldnames=['Фамилия', 'Имя', 'Телефон'])
            new_file.writeheader()
            new_file.writerows(res)


def change_data():
    with open('phone.csv', 'r+', encoding='UTF-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
        er_data = input("Введите Имя или фамилию, которую хотите поменять: ")
        print("erdata=" + str(er_data))
        for key in res:
            if key['Фамилия'] == er_data:
                print(key['Фамилия'])
                new_fam = input("На какую фамилию меняем?: ")
                key['Фамилия'] = new_fam
            if key['Имя'] == er_data:
                print(key['Имя'])
                new_name = input("На какое имя меняем?: ")
                key['Имя'] = new_name
        print(res)
        with open('phone.csv', 'w', encoding='UTF-8') as file:
            new_file = DictWriter(file, fieldnames=['Фамилия', 'Имя', 'Телефон'])
            new_file.writeheader()
            new_file.writerows(res)


def new_data():
        with open('phone.csv', 'a', encoding='UTF-8') as file:
            fam = input("Введите фамилию: ")
            name = input("Введите имя: ")
            ph_number = input("Введите номер телефона: ")
            new_user = {'Фамилия': fam, 'Имя': name, 'Телефон': ph_number}
            new_data = DictWriter(file, fieldnames=['Фамилия', 'Имя', 'Телефон'])
            new_data.writerow(new_user)


def main():
    print("Меню справчника:\n q - Выход\n r - Читать файл\n w - записать в файл(функция из семинара)\n new - Создать "
          "новую запись в справочнике\n ch - Изманить фамилию или имя в справочнике\n ed - удалить фамилию или имя в "
          "справочнике\n")
    while True:
        command = input("Выбрать опцию: ")
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                create_file()
            print(read_file('phone.csv'))
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
            write_file(get_info())
        elif command == 'ed':
            if not exists('phone.csv'):
                print('Справочник пуст!')
                break
            else:
                erase_data()
        elif command == 'ch':
            if not exists('phone.csv'):
                print('Справочник пуст')
                break
            else:
                change_data()
        elif command == 'new':
            if not exists('phone.csv'):
                create_file()
            else:
                new_data()


main()


