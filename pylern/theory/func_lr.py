def greet():
    print('Hellow')
    print('Good Morning!')


#greet()

# ВЫПОЛНЯЕТ ЗАДАЧУ

def add1(a,b):
    c=a+b
    print(c)


add1(4,5)


# ВОЗВРАЩАЕТ РЕЗУЛЬТАТ

def add2(x,y):
    z=x+y
    w = x-y
    return z, w

result = add2(6, 9) # (15, -3); or result1, result2 -->  15 -3
print(result)
result1,result2 = add2(7, 19)
print(result1, result2) # 26 -12