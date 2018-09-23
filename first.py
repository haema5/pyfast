# coding: utf-8

import os
import sys
import psutil

#

print("Hello world")
name = input("Your name: ")

print(name, ", welcome to Python!")

answer = input("Хочешь поработать? (Y/N)")

if answer == 'Y':
    print("Отлично, хозяин!")
    print("Я умею:")
    print("  1 - вывести список файлов")
    print("  2 - вывести информацию о системе")
    print("  3 - вывести список процессов")
    do = int(input("Что сделать? "))

    if do == 1:
        print(os.listdir())
    elif do == 2:
        print("Текущая директория: ", os.getcwd())
        print("Текущая платформа: ", sys.platform)
        print("Текущая кодировка ФС: ", sys.getfilesystemencoding())
        print("Текущий пользователь: ", os.getlogin())
        print("Количество процессоров: ", psutil.cpu_count())
    elif do == 3:
        print(psutil.pids())
    else:
        print("I don't know...")

elif answer == 'N':
    print("Goodbye!")
else:
    print("I don't know...")