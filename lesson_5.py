# словари и множества


# new = dict(name='azamat', age=20, country='kg')

# print(new)

# student = {
#     'name': 'Jack',
#     'age': 19,
#     'surname': 'ffack'
# }


# for key, value in student.items():
#     print(key,':',value)
# for i in student:
#     print(i, student[i])

# 


# print(student.keys()) выводит ключи
# print(student.values()) выводит тольео ключи
# print(student.items())выводит по парам кдюч и значение

# add 
# student['height'] = 1.76
# student['married'] = False
# student['hobby'] = ['english','chess','books']


# edit
# student['age'] += 1
# student['name'] += 'john'
# student.update(new)

# delete

# del student['surname']
# student.pop('age')




# expenses = {i: int(input(f'enter exp: for {i}')) for i in range(1,8)}

# for day,expenses in expenses.items():
#     print(f'{day}: {expenses}')

# print(sum(expenses.values())/ len(expenses))




#  множества



# num = [1,2,3,2,1,4,5,3]
# num2 = {1,2,3,2,1,4,5,3}

# print(num)
# print(num2)


# lagman = {'лапша','мясо','перец'}
# manty ={'тесто','мясо','лук'}

# print(lagman.difference(manty))
# print(lagman.symmetric_difference(manty))
# print(lagman.union(manty))
# print(lagman.intersection(manty))


