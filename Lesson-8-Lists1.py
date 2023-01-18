cities = ['New York','Moscow','new dehli','Sinferopol','Toronto']
print(cities)
#показывает длину списка
print(len(cities))
#показывает конкретное слово из списка
print(cities[1])
print(cities[-2])
#выводит с больщой буквы
print(cities[2].title())
#выводит все большими буквами
print(cities[2].upper())

cities[2] = 'Tula'

print(cities)

#добавляет в список в конец всегда
cities.append('Kursk')
cities.append('Yalta')
print(cities)

#добавляет в список на конкретное место, двигает того кто стоит на этом месте вперед
cities.insert(2,'Feodosiya')
print(cities)

#удаляет из списка по номеру, который стоит в списке
del cities [-1]
print(cities)

#удаляет конкретное слово в списке, но только один раз
cities.remove('Tula')
print(cities)

#выводит то, что было последнее удалено
deleted_city = cities.pop()
print('Deleted city is: ' + deleted_city)
print(cities)

#сортировка и реверсивная сортировка
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)

#выводит все с конца
cities.reverse()
print(cities)