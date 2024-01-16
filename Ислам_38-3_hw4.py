# mentors = ["Кубаныч", "Мирлан", "Гулина", "Камиля"]

# while True:
#     print("Список менторов:", mentors)
#     print("1. Добавление")
#     print("2. Изменение")
#     print("3. Удаление")
#     print("4. Выход")

#     choice = input("Выберите команду (1-4): ")

#     if choice == "1":  # Добавление
#         new_mentor = input("Введите имя нового ментора: ").capitalize()
#         if len(new_mentor) <= 15 and new_mentor not in mentors:
#             mentors.append(new_mentor)
#             print(f"Ментор {new_mentor} добавлен в список.")
#         else:
#             print("Некорректное имя или имя уже существует в списке.")

#     elif choice == "2":  # Изменение
#         old_mentor = input("Введите имя ментора, которого вы хотите заменить: ").capitalize()
#         new_mentor = input("Введите новое имя ментора: ").capitalize()

#         if old_mentor in mentors and len(new_mentor) <= 15 and new_mentor not in mentors:
#             index = mentors.index(old_mentor)
#             mentors[index] = new_mentor
#             print(f"Имя ментора {old_mentor} заменено на {new_mentor}.")
#         else:
#             print("Некорректные данные или ментор с таким именем не найден.")

#     elif choice == "3":  # Удаление
#         delete_option = input("Выберите вариант удаления (1 - по индексу, 2 - по имени): ")

#         if delete_option == "1":
#             try:
#                 index = int(input("Введите индекс ментора для удаления: "))
#                 deleted_mentor = mentors.pop(index)
#                 print(f"Ментор {deleted_mentor} удален из списка.")
#             except (ValueError, IndexError):
#                 print("Некорректный индекс.")

#         elif delete_option == "2":
#             delete_mentor = input("Введите имя ментора для удаления: ").capitalize()
#             if delete_mentor in mentors:
#                 mentors.remove(delete_mentor)
#                 print(f"Ментор {delete_mentor} удален из списка.")
#             else:
#                 print("Ментор с таким именем не найден.")

#     elif choice == "4":  # Выход
#         break

# mentors_tuple = tuple(mentors)
# print("Список менторов в виде кортежа:", mentors_tuple)
