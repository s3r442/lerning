
    # 1.  Дана некоторая строка с буквами и цифрами. Получите список позиций всех цифр из этой строки.

# x = 'fhq9eruyhf9834h57=01348h981rfuiqprufb'

# num_lst = []

# for char in x:
#     if char.isdigit():
#         num_lst.append(char)

# print(num_lst)



    # 2.  Дана некоторая строка Смените регистр букв на противоположный 'aBcDe'

# str_1 = 'AbCdE'

# str_2 = ''

# for index, char in enumerate(str_1,1):
#     if index%2 == 0:
#         str_2+= char.upper()
#     else:
#         str_2+= char.lower()

# print(str_2)




    # 3.  Дан некоторый список с числами Слейте пары элементов вместе: 12, 34, 56]

# nums_lst_1 = [1, 2, 3, 4, 5, 6]

# nums_lst_2 = []

# for i in range(0, len(nums_lst_1), 2):
#     comb = nums_lst_1[i]*10 + nums_lst_1[i+1]
#     nums_lst_2.append(comb)

# print(nums_lst_2)




    # 4. Дана некоторая строка Сделайте заглавным первый символ каждого второго слова в этой строке

# lower_str = 'aaa bbb ccc eee fff'

# up_str = ''

# for counter_1, char in enumerate(lower_str.split(' '),1):
#     if counter_1%2 == 0:
#         for counter_2, item in enumerate(char):
#             if counter_2 == 0:
#                 up_str+= item[0].upper()
#             else:
#                 up_str+=item.lower()
#         up_str+= ' '
#     else:
#         up_str+=char.lower() + ' '

# print(up_str)