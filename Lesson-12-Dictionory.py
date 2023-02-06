enemy = {
            'loc_x': 70,
            'loc_y': 50,
            'color': 'green',
            'health': 100,
            'name': 'Mudilo',
   
}

print(enemy)

print("Locattion X = " + str (enemy['loc_x']))
print("Location Y = " + str(enemy['loc_y']))
print("His name is: " + enemy['name'])

enemy['rank'] = 'Admiral'

print(enemy)

del enemy['rank']
print(enemy)

enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] - 30
if enemy['health'] < 80:
    enemy['color'] = 'yellow'


print(enemy)    

print(enemy.keys())
print(enemy.values())