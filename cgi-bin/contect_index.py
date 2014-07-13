#! /usr/bin/python3

import cgi

name_data = cgi.FieldStorage()
name = name_data['usrname'].value

try:
    with open('name.txt', "w") as data:
        print(str(name), file=data)
except IOError as err:
    print('File error: ' + str(err))
