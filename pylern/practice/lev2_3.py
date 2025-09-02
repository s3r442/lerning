
    # 1.  Даны два слова. Проверьте, что последняя буква первого слова совпадает с первой буквой второго слова.

# item  = 'lemon, melon'
# if item[4] == item[-1]:
#     print('ok')



    # 2.  Дана некоторая строка. Найдите позицию третьего нуля в строке.

# items = '1907p4y71g5f7251--1===1010304130501358'

# counter_1 = 0

# counter_2 = 0

# for item in items:
#     if item == '0':
#         counter_2 +=1
#         if counter_2 <= 3:
#             print('Нашла ноль №', counter_2, ', его индекс:', counter_1)
#         else:
#             break
#     counter_1+=1

# print('Задание выполнено')




    # 3. Даны числа, разделенные запятыми: '12,34,56' Найдите сумму этих чисел.

# nums = '12,34,56'

# result = int(nums[0:2])+int(nums[3:5])+int(nums[6:])

# result_1 = 0

# for num in nums.split(','):
#     print(num)
#     result_1+= int(num)
# print(result_1)

# print(result)


# def split_str(items):

#     words= []

#     for item in items.split(' - '):
#         print(item)
#         words.append(item)

#     return words


# print(split_str('hi - hellow - by - check'))




    # 4.  Дана дата в следующем формате:'2025-12-31' Преобразуйте эту дату в следующий словарь

# date = '2025-12-31'

# values = ['year', 'month', 'day']

# def date_lst(input_values):
#     data_lst = []
#     for value in input_values.split('-'):
#         data_lst.append(value)
#     return data_lst

# result = dict(zip(values, date_lst(date)))

# print(result)


# nums = [12,34,534,642,14,132]


# def sum_all(nums_lst):
#     return nums_lst*10


# print(list(map(sum_all, nums)))



    # 5. Дан словарь Получите сет его значений:{1, 2, 3, 4}

# dct_1 = {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3, 
# 	'd': 4,
# }

# set_dct_1 = set(dct_1.values())

# print(set_dct_1)