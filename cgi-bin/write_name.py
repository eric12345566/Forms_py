
name = "eric"

try:
    with open('name.txt', "w") as data:
         print(name , file=data)
except IOError as err:
    print('File error: ' + str(err)) 
