# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


# inp = inp.split()
#
# f_str = ''
# for i in range(len(inp)):
#     if inp[:i].count(inp[i]) == 0:
#         f_str += f'{inp[i]} '
#     else:
#         f_str += f'{inp[i]}_{inp[:i].count(inp[i])} '
#
# print(f_str)
#
# inp = 'a a a b c a a d c d d'
#
# new_str = ''
#
# dict = {}
#
# for element in inp.split():
#     if element not in dict:
#         dict[element] = 1
#         new_str += f'{element} '
#     else:
#         dict[element] += 1
#         new_str += f'{element}_{dict[element] - 1} '
# print(new_str)

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

inp = 'She sells sea shells on the sea shore The shells ' \
      'that she sells are sea shells I\'m sure.So if she sells sea ' \
      'shells on the sea shore I\'m sure that the shells are sea ' \
      'shore shells'

print(inp)

print(len(set(inp.lower().split())))
# list = set()
# stroka = ''
#
# for element in inp.lower():
#     if element != ' ':
#         stroka += f'{element}'
#     elif stroka not in list and stroka != '':
#         list.add(stroka)
#         stroka = ''
#     else:
#         stroka = ''
# list.add(stroka)
#
# print(len(list))
# print(list)

