x=1
i=0
while i!=16:
    print('# ', end=" ")
    i+=1
    if i%4==0:
        print()


a=0
for i in range(4):
    a+=1
    for i in range(a):
        print('# ', end=' ')      
        if a == 5:
            break
    print()

a=5
for i in range(4):
    a-=1
    for i in range(a):
        print('# ', end=' ')      
        if a == 0:
            break
    print()





# Task #1

y=['1','2','3','4']
for i in range(4):
    print(y, end=" ")
    y.pop(0)
    print()

# Task #2
n = ['A',"P","Q","R"]
i = 0
while i < 4:
    if i == 0:
        print(n)
    elif i == 1:
        n[1]='B'
        print(n)
    elif i == 2:
        n[2]='C'
        print(n)
    elif i == 3:
        n[3]='D'
        print(n)
    i+=1

    