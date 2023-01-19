
age = int(input("Geben Sie bitte Alter"))

if (age <=4):
    print("You are baby")
elif (age > 4) and (age < 12):
    print("You are kid")
elif (age >= 12) and (age < 19):
    print("You are teenager")
else:
    print("You are old!")

print("----------END---------")

all_cars = ['chrusler', 'dacia', 'bmw','KIA','vw','seat','skoda','lada','audi','ford','Chevrolet']
german_cars = ['bmw', 'vw', 'audi']

'''
if 'lada' in all_cars:
    print("Yes, Lada is in the List")
else:
    print("Lada not in the list")
'''

for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + " is German Car")
    else:
        print(xxxx + " is not German Car")

print("-----------END---------")