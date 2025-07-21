a = 10
b = a
print(id(a))
#140706560165064
print(id(b))
#140706560165064
print(id(10))
#140706560165064
k = 10
print(id(k))
#140706560165064
a = 9
print(id(a))
#140706560165032
print(b)
print(id(b))
k = a
print(id(k))
#140706560165032
b = 8
print(id(b))
#140706560165000
