# while True:
#     word = input("Введите слово на латинице или кириллице (рус, анг) или введите 'exit' для выхода: ")
    
#     if word.lower() == 'exit':
#         break
    

#     total_letters = len(word)
    
    
#     vowels = 0
#     consonants = 0
#     for letter in word:
#         if letter.lower() in "aeiouаеёиоуыэюя":
#             vowels += 1
#         elif letter.isalpha():
#             consonants += 1


#     if total_letters > 0:
#         vowels_percentage = (vowels / total_letters) * 100
#         consonants_percentage = (consonants / total_letters) * 100
#     else:
#         vowels_percentage = 0
#         consonants_percentage = 0
    
    
#     print(f"Общее количество букв: {total_letters}")
#     print(f"Количество гласных: {vowels}")
#     print(f"Количество согласных: {consonants}")
#     print(f"Процент гласных: {vowels_percentage:.2f}%")
#     print(f"Процент согласных: {consonants_percentage:.2f}%")
#     print("-----------------------------")

# list1 = [1,2,3,4,5,6,7,8,9,10]
# index = list1.index(2)
# list1[index] = 200
# print(list1)

# list1 = ['shdj', '', 'gdhsjhgdhsj', '','gfyhdsjkjhdj','gfgfgf']
# relist1 = list(filter(None, list1))
# print(relist1)

# list1 = [1,2,3,45,6,78,9]
# res = [x * x for x in list1]
# print(res)

# list1 = [5, 20, 15, 20, 25, 50, 20]
# def removeValue(sampleList, val):
#    return [value for value in sampleList if value != val]
# resList = removeValue(list1, 20)
# print(resList)



# list1 = ['hdsjhd','shdjk','shdjjs','sdhsuhd']
# list1 = (list1[::-1])
# print(list1)




# mentors = ['Кубаныч', 'Гулина', 'Мирлан','Камила']

# while True:
#     print('добавить, удалить, изменить, выход')
#     ask = input('выберите команду :')
#     if ask == 'добавить':
#         add = input('кого добваить :').title()
#         if len(add) < 15 :
#             if add not in mentors :
#                 mentors.append(add)
#             else:
#                 print('это имя уже в списке !!!')
#         else:
#             print('имя не должно превышать 15 букв')
#     elif ask == 'изменить':
#         add1 = input('кого заменить? :').title()
#         if add1 in mentors:
#             men = input('на кого заменить? :').title()
#             if len(men) < 15 :
#                 if men not in mentors :
#                     index = mentors.index(add1)
#                     mentors[index] = men
#                 else:
#                     print('это имя уже в списке !!!')
#             else:
#                 print('имя не должно превышать 15 букв')
#         else:
#             print('такого имени нет в списке!')
#     elif ask == 'удалить':
#         add2 = input('удалить по индексу или по имени? :')
#         if add2 == 'по индексу':
#             qst = int(input('какой индекс хотите удалить? :' ))
#             if len(mentors) >= qst and qst > 0:
#                 mentors.pop(qst - 1 )
#             else:
#                 print('не правильный индекс!!!')
#         elif add2 == 'по имени':
#             qst1 = input('какое имя удалить?:').title()
#             if qst1 in mentors:
#                 mentors.remove(qst1)
#             else:
#                 print('этого имени нет в списке!!!')
#         else:
#             print('введено не корректно!!!')        

#     elif ask == 'выход':
#         break
#     else:
#         print('введено не корректно!!!')

#     print(mentors)


# print(tuple(mentors))


# def max1(*args):
#     max_value = args[0]
#     for value in args:
#         if value > max_value:
#             max_value = value
#     return max_value
    
# def min1(*args):
#     min_value = args[0]
#     for value in args:
#         if value < max_value:
#             min_value = value
#     return min_value





def add_movie(movies, movie_name):
    movie_name = movie_name.capitalize()
    if movie_name not in movies:
        movies[movie_name] = {}
        print("Movie added successfully")
    else:
        print("This movie already exists!")

def add_rating(movies, movie_name, user_name, rating):
    movie_name = movie_name.capitalize()
    if movie_name in movies:
        if user_name not in movies[movie_name]:
            if 0 <= rating <= 10:
                movies[movie_name][user_name] = rating
                print(f"A rating has been added for {movie_name}: {user_name} rated it {rating}")
            else:
                print("Invalid rating. Please enter a rating between 0 and 10.")
        else:
            print("User with this name already rated the movie. Please enter a different user name.")
    else:
        print("This movie doesn't exist")

def display_ratings(movies):
    for movie_name, ratings in movies.items():
        if ratings:
            average_rating = sum(ratings.values()) / len(ratings)
            print(f"{movie_name} is rated {average_rating:.1f}")
        else:
            print(f"Rating is not yet available for {movie_name}")

def find_movie(movies, movie_name):
    movie_name = movie_name.capitalize()
    return movies.get(movie_name, None)

movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },
    "Troy": {}
}

while True:
    print("\nCommands:")
    print("1. Add Movie")
    print("2. Add Rating")
    print("3. Display Ratings")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        movie_name = input("Enter the movie name: ")
        add_movie(movies, movie_name)

    elif choice == "2":
        movie_name = input("Enter the movie name: ")
        movie = find_movie(movies, movie_name)
        if movie:
            user_name = input("Enter the user name: ")
            rating = int(input("Enter the rating (0-10): "))
            add_rating(movies, movie_name, user_name, rating)
        else:
            print("This movie doesn't exist")

    elif choice == "3":
        display_ratings(movies)

    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
