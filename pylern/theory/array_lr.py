import array as arr

vals= arr.array('i',[10,203,130])
vals2 =arr.array('u', ['a', 'b','s'])
vals3= arr.array(vals2.typecode,(val for val in vals2))
vals4= arr.array(vals.typecode,(val*val for val in vals))
print(vals[1])
print(vals.buffer_info())
#vals.append()
#vals.extend()
#vals.remove()
#vals.pop()

for i in vals3: #range(len(vals3)):
    print(i)

for e in vals4: 
    print(e)

x = 0
while x < len(vals3):
    print(vals3[x])
    x+=1

arr1 = arr.array('i', [])
len1 = int(input('Enter the length of the array: '))
for z in range(len1):
    n = int(input('Enter your item: '))
    arr1.append(n)

for h in arr1:
    print(h, end=' ')
print()


k = 0
find = int(input('Array value for search ')) 
for value in arr1:
    if value == find:
        print('Index = ' + str(k))
        break
    k+=1

print('Index =', arr1.index(find))


