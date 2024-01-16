# # переменная хранящая строку
# message = input('ведите строку :')
# # количество повторений
# count = int(input('введите число :'))

# for i in range(count):

#     print(message)







# time = input('enter time: ').lower()

# if time == 'morning' or time == 'утро':
#     print('good morning')
# elif time == 'day' or time == 'день':
#     print('good afternoon')
# elif time == 'evening' or time == 'вечер':
#     print('good evening')
# else:
#     print('i dont\'t know time')



# 5 декабря 16:00, Цыклы


# c = 0 

# while c < 100:
#     answer = input('enter y or stop :')
#     if answer == 'stop':
#         print('программа завершена')
#         break
#     print('geegs', c)
#     c +=1



# word = 'python'
# for i in  word:
#     if i == 't':
#         continue
#     print(i)




# word = 'python'
# print(word[0:3])
# print(word[::-1])


# word = '123456789'
# print(word[::2])

# counter = 0 
# for i in range(1, 8):
#     counter == int(input(f'enter exp for day {i}:'))

# print(counter)


# cash = 1000 
# percents = 0.15
# years = 5 


# for year in range(1, years+1):
#     cash += cash * percents
#     print(f"{year}:{'%.2f' % cash}")


# №1
# def  summa(first, second):
#     return first + second

# def sub(first, second):
#     return first - second

# def mult(first, second):
#     return first * second

# def div(first, second):
#     return first / second


# num = int(input('введите первое значение:'))
# num1 = int(input('введите второе значение:'))

# print(f'сумма значений: {summa(num, num1)} , минус: {sub(num, num1)},'f' умножение: {mult(num, num1)}, деление: {div(num, num1)}')



#№2
# def even_or_odd(a):    
#     # num1 = int(input('введите любое число:'))
#     if a % 2 == 0:
#         return('четное число')
#     else:
#         return('нечетное число')
    
# print()

    
# def проверка_четности(число):
#     if число % 2 == 0:
#         return "Число {} четное.".format(число)
#     else:
#         return "Число {} нечетное.".format(число)

# # Пример использования функции
# ваше_число = 77790
# результат = проверка_четности(ваше_число)
# print(результат)