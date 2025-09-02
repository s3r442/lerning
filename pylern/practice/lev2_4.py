
    # 1.  Дана некоторая строка с буквами и цифрами. Получите позицию первой цифры в этой строке.

# nums_str = 'hf91f4h81431h43'


# for index, item in enumerate(nums_str):
#     print(item)
#     if item.isdigit():
#         print(index, '-', item)
#         break



    
     # 2.  Дано число. Выведите в консоль количество четных цифр в этом числе.

# num = 1476439321898

# def num_even_finder(number):
    
#     num_str_1 = str(number)

#     counter_2 = 0

#     for counter_1, item in enumerate(num_str_1):
#         if int(item)%2 == 0:
#             counter_2+=1
#             print('Number:', item, 'Index:', counter_1, 'Total number:', counter_2)

# print(num_even_finder(num))




    # 3.  Дан словарь Получите список его ключей:['a', 'b', 'c', 'd']

# dct_1 = {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3, 
# 	'd': 4,
# }

# print(list(dct_1.keys())) 



    # 4.  Дана некоторая строка Переведите в верхний регистр все нечетные буквы этой строки.

# str_1 = 'abcde'

# res = ''

# for index, char in enumerate(str_1):
#     if index%2==0:
#         res +=char.upper()
#     else:
#         res+= char
# print(res)




    # 5.  Дана некоторая строка со словами Сделайте заглавным первый символ каждого слова в этой строке.

# str_1 = 'aaa bbb ccc'

# def upper_0_index(str_lower):
    
#     str_up_0 = ''

#     for char in str_lower.split(' '):
#         for index,item in enumerate(char):
#             if index == 0:
#                 str_up_0+= item.upper()
#             else:
#                 str_up_0+= item
#         str_up_0+= ' '
#         # up_0_index= (char[0].upper() +char[1] +char[2] + ' ')
#         # str_up_0 += up_0_index
#     return str_up_0


# print(upper_0_index(str_1)) 




    # 6. Дана дата в следующем формате Преобразуйте эту дату в следующий кортеж: ('31', '12', '2025')

# str_1 = '2025-12-31'

# lst_1 = []

# for num in str_1.split('-'):
#     lst_1.insert(0,num)
#     tpl_1=tuple(lst_1)
# print(tpl_1)