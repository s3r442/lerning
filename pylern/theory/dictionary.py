x = {1:'melon',2:'watermelon',3:'lemon'}
#dictionary (словарь) - позволяет присваевать элементам ключи (keys), для упращения кода
print(x)
print(x[3])
print(x.get(1))
print(x.get(5, 'Not Found'))
#обращаясь к ключам мы можем выводить их значение из словаря
y = ['I', 'You', 'They', 'She']
z = ['Melon', 'Watermelon', 'Lemon', 'Strawberry']
data = dict(zip(y,z))
#словари можно формировать из списков
print(data)
print(data['I'])
data['He'] = "Banan"
print(data)
del data['She']
#можем удалять\добавлять ключи и заменять их значение
print(data)
fruits = {'I': ['apples', 'peaches'], 'You': {'apples': ['red','green'],'banans': ['blue','yellow']}}
print(fruits['You'])
print(fruits['You']['banans'])
print(fruits['You']['banans'][1])
fruits['You']['banans'][1] = 'red'
print(fruits['You']['banans'][1])
#создавая сложные словари, мы можем обращаться к каждому элементу напрямую