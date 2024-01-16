# movies = {

#     "Django Unchained": {

#         "John": 10,

#         "Jack": 9

#     },

#     "Troy": {}

# }


# def add_1(movie):
#     if movie not in movies:
#         movies[movie] = {}
#         print('Movie added successfully')
#     else:
#         print('This movie already exist!')

# def add_2(rating):
#     nums = {}
#     if rating in movies:
#         while True:
#             user = input('Ведите имя: ')
#             if user not in movies[rating]:
#                 qsn = int(input('Оцените этот фильм 0 до 10:'))
#                 if qsn >= 0 and qsn <= 10 :
#                     nums[user] = qsn
#                     movies[rating].update(nums)
#                     print(f'A rating has been added for Interstellar: {user} rated it {qsn} ')
#                 else:
#                     print('Ты тупой? Сказано же от 0 до 10 !!!')
#                 break
#             else:
#                 print('Это имя уже занято. Напиши другое имя')
#     else:
#         print("This movie doesn't exist")


# def look(movies):
#     for i in movies.keys():
#         count = 0
#         sum1 = 0
#         if len(movies[i]) != 0:
#             for j in movies[i].values():
#                 sum1 += j
#                 count += 1
#             everich = sum1 / count
#             print(f'{i} is rated {round(everich,1)}')
#         else:
#             print(f'Rating is not yet available for {i}')    



# while True:
#     print("1. Добавить фильм")
#     print("2. Добавить рейтинг к фильму ")
#     print("3. Посмотреть рейтинги фильмов")
#     print("4. Выход")

#     pop = input('Что вы хотите сделать?:')
#     if pop == '1':
#         pop1 = input('Введите название фильма:').title()
#         add_1(pop1)
#     elif pop == '2':
#         pop2 = input('Какой фильм хотите оценить?:').title()
#         add_2(pop2)
#     elif pop == '3':
#         look(movies)
#     else:
#         break

