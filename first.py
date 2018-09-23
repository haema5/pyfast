# coding: utf-8

import os
import sys
import psutil

#

print("Hello world")
#name = input("Your name: ")

#print(name, ", welcome to Python!")

answer = input("Хочешь поработать? (Y/N)")

if answer == 'Y':
    print("Отлично, хозяин!")
    print("Я умею:")
    print("  1 - вывести список файлов")
    print("  2 - имя текущей директории")
    print("  3 - вывести список процессов")
    print("  4 - платформа (ОС)")
    print("  5 - кодировка")
    print("  6 - логин")
    print("  7 - количество ЦПУ")
    do = int(input("Что сделать? "))

    if do == 1:
        print(os.listdir())
    elif do == 2:
        print(os.getcwd())
    elif do == 3:
        print(psutil.pids())
    elif do == 4:
        print(sys.platform)
    elif do == 5:
        print(sys.getfilesystemencoding())
    elif do == 6:
        print(os.getlogin())
    elif do == 7:
        print(psutil.cpu_count())
    else:
        print("I don't know...")

elif answer == 'N':
    print("Goodbye!")
else:
    print("I don't know...")