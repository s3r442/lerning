
    # 1.  Дан список с числами. Подсчитайте количество отрицательных чисел в этом списке.

# nums = [1,-2, 4,-5, 1, 3, -7, 2, 0, -6]

# item = 0

# print(nums)

# for num in nums:
#     if num < 0:
#         item+=1
#         print(num, end=' ')

# print()
# print('Negative nums in list =', item)



    # 2.  Дан список с числами. Оставьте в нем только положительные числа.

# nums = [1,-2, 4,-5, 1, 3, -7, 2, 0, -6]

# item = 0

# print(nums)

# for num in nums:
#     if num > 0:
#         item+=1
#         print(num, end=' ')

# print()
# print('Posiive nums in list =', item)



    # 3.  Дана строка. Удалите предпоследний символ из этой строки.

# str1 = 'qiurhgtoqirng'

# res = ''

# str1 = list(str1)
# del str1[-2]

# for i in str1:
#     res = res + i

# print(res)



    # 4.  Дан список со строками. Оставьте в этом списке только те строки, которые заканчиваются на .html.

# lst1 =[ 
#     '.html.wergwegwe',
#     'qerqregtrwq',
#     '.html.qergerqg',
#     'qergeqrgqer',
#     '.html.htuejhetyn',
#     '.html.vnvjflaaetg'
# ]

# item = 0

# for i in lst1:
#     if lst1[item][0:6] == '.html.':
#         print(i, end=', ')
#     item+=1



    # 5.  Дан список с дробями Округлите эти дроби до одного знака в дробной части.

# fl_nums = [1.456, 2.125, 3.32, 4.1, 5.34]

# for fl_num in fl_nums:
#     fl_num = round(fl_num, 1)
#     print(fl_num, end= ', ')



    # 6.  Дан словарь  Получите список его значений: [1, 2, 3, 4]

dict1 = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}

dict_vals = list(dict1.values())

print(dict_vals)