# работа с файлами 

# w - write (запись)
# a - add (добовляет)
# x - создание файла без повторения имен
# r - чтение файла


# file = open('new_file.txt', 'w')
# file.write('бишкекб гигс')
# file.close()


# with open('new_file.txt', 'a') as file:
    # file.write('\nвторая строка2!')


# with open('new_file1.txt', 'x') as new_file:
#     new_file('123')


# with open('new_file.txt', 'r') as file:
#     print(file.read())
# #     print(file.readlines()[-5])
# from time import sleep
    

# with open('new_file.txt','r') as file:
#     for i in file.read():
#         sleep(1)
#         print(i, end= '')

data = {}

with open('resultat.txt') as file:
    file.readline()
    file.readline()
    # rates = [int(i) for i in file.read
    for i in file.readlines():
        data[i.split()[0]] = int(i.split()[-1])


print(sum(data.values()) / len(data))

data = sorted(data.items(), key=lambda x: x[1], reverse=True)
print(data)