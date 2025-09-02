
    # 1.  Дана некоторая строка Получите сет позиций всех нулей в этой в строке.

# str_vs_0 = '023m0df0dfg0'

# def find_0_ind(str_1):
    
#     count_1 = 0

#     lst_1 = []

#     for count_2, item in enumerate(str_1):
#         if item == '0':
#             count_1+=1
#             print('0 №:', count_1, 'index:',count_2)
#             lst_1.append(count_2)
    
#     print('Сет индексов:', lst_1, 'Общее кол-во 0:', count_1)

# find_0_ind(str_vs_0)





    # 2.  Дана некоторая строка Удалите из этой строки каждый третий символ.

# str_1 = 'abcdefg'

# str_2 = ''

# for index, item in enumerate(str_1,1):
#     if index%3 != 0:
#         str_2+=item
#     else:
#         continue
# print(str_2)




    # 3.  Дан некоторый список Поделите сумму элементов, стоящих на четных позициях, 
    # на сумму элементов, стоящих на нечетных позициях.

# nums = [1, 2, 3, 4, 5, 6]

# odd_nums = []

# even_nums = []

# for index, num in enumerate(nums,1):
#     if index%2 != 0:
#         odd_nums.append(num)
#     else:
#         even_nums.append(num)

# result = sum(even_nums)/sum(odd_nums)

# print(result)




    # 4.  Дана дата Преобразуйте эту дату в следующий кортеж: ('31', '12', '2025')

# data_lst_1 = ['2025', '12', '31']

# data_lst_2 = []

# for item in data_lst_1:
#     data_lst_2.insert(0,item)
# data_tpl = tuple(data_lst_2)

# print(data_tpl)