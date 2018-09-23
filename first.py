# coding: utf-8

import os
import psutil

#

print("Hello world")
#name = input("Your name: ")

#print(name, ", welcome to Python!")

answer = input("Хочешь поработать? (Y/N)")

if answer == 'Y':
    print("Отлично, хозяин!")
    print("Я умею:")
    print("  1 - вывести список файлов;")
    print("  2 - вывести информацию о системе.")
    do = int(input("Что сделать? "))

    if do == 1:
        print(os.listdir())
    elif do == 2:
        psutil.pids()
    else:
        pass
elif answer == 'N':
    print("Goodbye!")
else:
    print("I don't know...")