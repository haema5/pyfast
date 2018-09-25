# coding: utf-8

import os
import sys
import shutil
import psutil


def dupl_file(filename):
    newfile = filename + '.dupl'
    shutil.copy(filename, newfile)
    if os.path.exists(newfile):
        print("Файл ", newfile, " был успешно создан")
        return True
    else:
        print("Ошибка! ", newfile, " не был создан")
        return False


def del_file(dir_name):
    x = 0
    file_list = os.listdir(dir_name)
    for f in file_list:
        long_name = os.path.join(dir_name, f)
        if long_name.endswith('.dupl'):
            os.remove(long_name)
            x += 1
    return str(x)


def sys_info():
    print("Текущая директория: ", os.getcwd())
    print("Текущая платформа: ", sys.platform)
    print("Текущая кодировка ФС: ", sys.getfilesystemencoding())
    print("Текущий пользователь: ", os.getlogin())
    print("Количество процессоров: ", psutil.cpu_count())


#

print("Привет!")
name = input("Как тебя зовут?: ")

print(name, ", рад познакомиться с тобой!")

answer = ''
while answer != 'q':
    answer = input("Хочешь поработать? (y-Да/n-Нет/q-Выйти) ")
    if answer == 'y':
        print("Отлично!")
        print("Я умею делать следующие вещи:")
        print("  1 - вывести список файлов")
        print("  2 - вывести информацию о системе")
        print("  3 - вывести список процессов")
        print("  4 - продублировать все файлы в дирректории " + os.getcwd())
        print("  5 - дублировать определенный файл")
        print("  6 - удалить файлы .dupl")
        print('')
        do = int(input("Чем могу помочь? "))
        if do == 1:
            print(os.listdir())
        elif do == 2:
            sys_info()
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print("Дублируем файлы...")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                if os.path.isfile(file_list[i]):
                    if file_list[i] != '.git':
                        dupl_file(file_list[i])
                i += 1
        elif do == 5:
            filename = input("Какой файл дублировать? ")
            if os.path.isfile(filename):
                dupl_file(filename)

        elif do == 6:
            dirname = input('Укажите имя директории: ')
            print(del_file(dirname) + ' файла(ов) удален(о) в директории <' + os.path.abspath(dirname) + '\>!')

        else:
            pass
    elif answer == 'n':
        print("Очень жалко, но я хочу работать! Жми <y>!")
    else:
        print("Я не понимаю тебя...")
