# coding: utf-8

import os
import sys
import shutil
import psutil

#

print("Hello world")
name = input("Your name: ")

print(name, ", welcome to Python!")

answer = ''
while answer != 'q':
    answer = input("Хочешь поработать? (y/n/q)")
    if answer == 'y':
        print("Отлично, хозяин!")
        print("Я умею:")
        print("  1 - вывести список файлов")
        print("  2 - вывести информацию о системе")
        print("  3 - вывести список процессов")
        print("  4 - продублировать файлы")
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
        elif do == 4:
            print("Дублируем файлы")
            file_list = os.listdir()
            print(os.listdir())
            # duplicate all files
            print(file_list)
            i = 0
            while i < len(file_list):
                print(file_list[i])
                if os.path.isfile(file_list[i]):
                    if file_list[i] != '.git':
                        newfile = file_list[i] + '.dupl'
                        shutil.copy(file_list[i], newfile)
                i += 1
        elif do == 4:
            print("Дублируем файлы")
            file_list = os.listdir()
            print(os.listdir())
            # duplicate all files
            print(file_list)
            i = 0
            while i < len(file_list):
                print(file_list[i])
                if os.path.isfile(file_list[i]):
                    if file_list[i] != '.git':
                        newfile = file_list[i] + '.dupl'
                        shutil.copy(file_list[i], newfile)
                i += 1
        else:
            pass


    elif answer == 'n':
        print("Goodbye!")
    else:
        print("I don't know...")
