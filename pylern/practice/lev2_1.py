
    # 1.  Дан список со строками. Оставьте в этом списке только те строки, которые начинаются на http://.

# lst1 = [
#     'http://qrferqfre', 
#     'eqrfqe',
#     'http://qrefsvm',
#     'fwofjire',
#     'http://werfonoe',
#     'ewo;foef',
#     'http://weoirfbt',
#     'qeroirmqp',
#     'http://rqeogjeq']

# print(lst1)

# item = 0

# for _ in lst1:
#     if lst1[item][0:7] != 'http://':
#         del lst1[item]
#     item+=1
   
# print("Only 'http://':", lst1)



    # 2.  Дана некоторая строка. Найдите позицию первого нуля в строке.

# str1 = '1740yf078g0143f1034-88hf74g-097'

# for i in str1:
#     if i == '0':
#         print(i,', zero index:', str1.index(i))
#         break



    # 3.  Дан список. Удалите из него элементы с заданным значением.

# lst1 = ['hi', 'no', 'hi', 'yes', 'melone', 'hi', 'print']

# print(lst1)

# item = 0

# for i in lst1:
#     if i == 'hi':
#         del lst1[item]
#     item+=1

# print(lst1)



    # 4.  Выведите в консоль все числа в промежутке от 10 до 1000, сумма первой и второй цифры которых равна пяти.

# for num in range(10,1001):
#     num= str(num)
#     res = int(num[0]) + int(num[1])
#     if res == 5:
#         print(num, end=' ')



    # 5.  Дана некоторая строка Очистите ее от дублей символов

# str1 = 'abcdeabc'

# set1 = set()

# res = ''

# for i in str1:
#     if i not in set1:
#         set1.add(i)
#         res= res + i

# print(res)