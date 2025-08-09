nums = [3,12.07,'melon',True]
#list variable - variable with multiple values - muteble
names = ['sugar','salt','pepper','watermelon']
print(nums)
print(nums[1])
print(nums[-2])
print(nums[2:])
print(nums[:2])
print('weight: ' + str(nums[0])+'\nprise: '+str(nums[1])+'\ntype: '+nums[2]+'\non stock: '+str(nums[3]))
#можем вызывать отдельные элементы списка
resultum = [nums, names]
#можем создавать списки из списков
print(resultum)
nums.append(False)
#добавляет элемент в конец списка
nums.insert(3,"pool")
#добавляет элемент на место выбранного индекса
nums.remove(12.07)
#удаляет выбранный элемент
nums.pop(3)
#удаляет элемент под выбранным индексом
del names[2:]
#удаляет несколько элементов списка
names.extend(["hellow",'bye','good'])
#добавляет несколько элементов в список
print(nums)
print(names)
print(min(nums))
#output min item
print(max(nums))
#output max item
print(sum(nums))
#output sum of items
print(nums.sort())
#output sort items