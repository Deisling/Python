
#         0    1      2      3       4
cars = ['bmw','vw','seat','skoda','lada']

#заходит в цикл и по одному печатает с большой буквы
for x in cars:
    print(x.upper())

#выводит лист от одного до пяти
for x in range(1,6):
    print(x)

#создали массив от одного до девяти
mynumber_list = list(range(0,10))
print(mynumber_list)
print('===================================')

for x in mynumber_list:
    x = x*2
    print(x)


mynumber_list.sort(reverse=True)
print(mynumber_list)

#выводит максимум, минимум и сумму массива
print('Max number is: ' + str(max(mynumber_list)))
print('Min number is: ' + str(min(mynumber_list)))
print('Sum of list is: ' +str(sum(mynumber_list)))

print('=============================================')


#         0    1      2      3       4
cars = ['bmw','vw','seat','skoda','lada']

#выводит элементы из массива с 1 по 3
mycars = cars[1:4]
print(mycars)

mycars = cars[:4]
print(mycars)

mycars = cars[-3:-1]
print(mycars)



#клонировать массивы, чтобы не изменялась одновременно инофрмация в двух массивах
#         0    1      2      3       4
cars = ['bmw','vw','seat','skoda','lada']
mycars = cars[:]

