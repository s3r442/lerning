x = 5
i = 1
while i<=x:
    if x>10:
        print('out of stock')
        break
    else:
        print('Candy', end=" ")
        i+=1
print()

x = 3
i = 1
av = 10
while i<=x:
    print('Candy', end=" ")
    i+=1
    if i > av:
        print('out of stock')
        break
print()

for i in range(1,15):
    if i%2==0:
        continue
    print(i, end=" ")
print()
print('Bye')

for i in range(40):
    if i%2!=0:
        pass
    else:
        print(i)





# Task #1

i =True
while i:
    x =input('Enter your number or print "stop": ')
    if x=='stop':
        print('Bye!')
        break
    elif int(x)%2==0:
        print('Not prime')
    else :
        print('Prime')
        