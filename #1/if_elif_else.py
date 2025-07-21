r=int(input())%2
print(r)
if r==0:
    print('Hi')
    if r>5:
        print('Good')
    else:
        print('Bad')
else:
    print('Bye')
x=2
if x==1:
    print('One')
elif x==2:
    print('Two')
elif x==3:
    print('Three')
else:
    print('Any num')


#Task #1
z = int(input('Enter num: '))
if z <= 5:
    print('True')
else:
    print('False')


#Task #2
h = {
'1st':int(input('Enter 1st num: ')),
'2nd': int(input('Enter 2nd num: ')),
'3rd':int(input('Enter 3rd num: '))
}
if h['1st']>h['2nd'] and h['1st']>h['3rd']:
    print(str(h['1st'])+" - It's the greatest number!")
elif  h['2nd']>h['1st'] and h['2nd']>h['3rd']:
    print(str(h['2nd'])+" - It's the greatest number!")
elif h['3rd']>h['1st'] and h['3rd']>h['2nd']:
    print(str(h['3rd'])+" - It's the greatest number!")
else:
    print("All numbers are equal!")