from cmath import *
import numpy as np


c = np.array([1,2,4,5]) # == int64; or np.array([1,2,4,5], float) == float64
print(c.dtype)

c = np.array([1,2,4,5.0]) # == float64; or np.array([1,2,4,5.0], int) == int64
print(c.dtype)

lin = np.linspace(0, 4, 3) #[0. 2. 4.]
print(lin)

aran= np.arange(1,10,4) #[1 5 9]
print(aran)

logs = np.logspace(1, 10, 5) #[1.00000000e+01 1.77827941e+03 3.16227766e+05 5.62341325e+07 1.00000000e+10]
print(logs)

zr = np.zeros(5) # == float64; or np.zeros(5, int) == int64
print(zr)

on = np.ones(5)  # == float64; or np.ones (5, int) == int64
print(on)

inu=0
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([1,5,2,4,6])
for i in arr1:
    e = i +5
    arr1[inu] = e
    inu+=1
    print(e)
print(arr1)

arr1 -=5
print(arr1)

arr3 = arr1+arr2
print(arr3)

print(np.cos(arr1)) #np.log/ np.cos/ np.sqr/ np.sum/ np.min/ np.max/ np.sort/ np.unic/ np.concatenate/
print(np.concatenate([arr1, arr2]))


arra1 = np.array([
    [1,2,3,5,7,2],
    [4,5,6,1,4,7]
    ])

print(arra1)
print(arra1.dtype) # == int64
print(arra1.ndim)  # == 2
print(arra1.shape) # == (2, 6)
print(arra1.size)  # == 12

arra2 = arra1.copy().flatten()
print(arra2) # == [1 2 3 5 7 2 4 5 6 1 4 7]

arra3 = arra2.reshape(3,4)

print(arra3) # [[1 2 3 5]
#               [7 2 4 5]
#               [6 1 4 7]]

arra4 = arra1.reshape(2,2,3)
print(arra4) # [[[1 2 3]
#                [5 7 2]]
#
#               [[4 5 6]
#                [1 4 7]]]

# SHALLOW COPY (поверхостное)

arr4 = arr1
print(arr4) # псевдоним массива

arr5 = arr1.view()
print(arr5)
print(id(arr1)) #id 3258539834704 --> [1 2 3 4 5]
print(id(arr4)) #id 3258539834704 --> [1 2 3 4 5] 
print(id(arr5)) #id 3258557533248 --> [1 2 3 4 5]

arr1[1] = 12
print(arr1) #id 3258539834704 --> [1 12 3 4 5]
print(arr4) #id 3258539834704 --> [1 12 3 4 5] 
print(arr5) #id 3258557533248 --> [1 12 3 4 5]

# DEEP COOPY (глубокое)

arr6= arr1.copy()
print(arr1, id(arr1)) #id 3258539834704 --> [1 12 3 4 5]
print(arr6, id(arr6)) #id  4766592863072 --> [1 12 3 4 5]

arr1[1] = 25
print(arr1, id(arr1)) #id 3258539834704 --> [1 25 3 4 5]
print(arr6, id(arr6)) #id  4766592863072 --> [1 12 3 4 5]

# MATRIX

rra1 = np.array(
    [[1, 12, 3, 4],
     [2, 13, 7, 5]]
     )
m = np.matrix(rra1)
print(m)

tc1 = np.matrix('1 2 3 4 ; 5 6 7 8')
print(tc1) # [[1 2 3 4]
#            [5 6 7 8]]

tc1 = np.matrix('1 2 3 ; 4 5 6 ; 7 8 9')
print(tc1) # [[1 2 3]
#            [4 5 6]
#            [7 8 9]]

print(np.diagonal(tc1)) # [1 5 9]

print(tc1.min()) # == 1
print(tc1.max()) # == 9

tc2 = np.matrix('1 2 3 ; 4 5 6 ; 7 8 9')

tc3=tc1+tc2
print(tc3) # [[ 2  4  6]
#             [ 8 10 12]
#             [14 16 18]]

tc3=tc1*tc2
print(tc3) # [[ 30  36  42]
#             [ 66  81  96]
#             [102 126 150]]