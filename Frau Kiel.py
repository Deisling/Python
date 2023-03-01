'''
#####Aufgabe 1#####
#Brutto-Netto-Rechner

bruttopreis = 500
mwst = 19

#Berechnung und Ausgabe
nettopreis = bruttopreis/(100+mwst)*100
print("Der Nettopreis ist", nettopreis)
'''


'''
#####Aufgabe 2#####
#Zahlenspiel

zahl = 12
ergebnis = zahl*2
ergebnis = ergebnis*5
ergebnis = ergebnis/zahl
ergebnis = ergebnis-7
print(ergebnis)
'''


'''
#Null
number = int(input("Bitte Zahl eingeben"))
if (number > 0):
    print("Gut")
elif (number < 0):
    print("Negativ")
else:
    print("Null")
'''

'''
number = int(input("Bitte ein Zahl eingeben"))
if (number > 0):
    print("Gut")
elif (number < 0):
    print("Negativ")
else:
    print("Null")
'''

'''
##### AUFGABE1 #####
# sowohl x, y als auch z haben am Ende den gleichen Wert, 5 (x+y)
print("Aufgabe1")
x=2
y=3
z=x+y
x=z
y=x
print(x)
print(y)
print(z)
'''


'''
##### AUFGABE2 #####
# Berechnung des Wunschschnittes
print("Aufgabe2")

note1 = 2
note2 = 3
note3 = 2
wunschschnitt = 2

benoetigteNote = wunschschnitt*4-note1-note2-note3
print(benoetigteNote)
'''


'''
##### AUFGABE3 #####
# Zeitangabe in Sekunden
print("Aufgabe3")

stunden = 2
minuten = 43
sekunden = 33

print(stunden*60*60 + minuten*60 + sekunden)
'''


'''
##### AUFGABE4 #####
# Maschinengebühren
print("Aufgabe4")

grundgebuehr = int(input("grundgebuehr"))
stundengebuehr = int(input("stundengebuehr"))
anzahlStunden = int(input("anzahlStunden"))


preis = grundgebuehr+stundengebuehr*anzahlStunden
print("Das kostet",preis)
'''


'''
##### AUFGABE5 #####
#Transporte mit Lieferwagen und Lastwagen
print("Aufgabe5")

lieferwagen = int(input("lieferwagen"))
lastwagen = int(input("lastwagen"))
kmLieferwagen = int(input("kmLieferwagen"))
kmLastwagen = int(input("kmLastwagen"))

preisTransport = lieferwagen*kmLieferwagen+lastwagen*kmLastwagen
print("Preis ist", preisTransport)
'''

'''#### AUFGABE5 #####
# Weinhändler
print("Aufgabe6")

preisRot = 18
preisRose = 13
preisWeiss = 12

anzahlRot = 12
anzahlRose = 6
anzahlWeiss = 24

preisWein = preisRot*anzahlRot+preisRose*anzahlRose+preisWeiss*anzahlWeiss
print("Preis ist", preisWein)
'''

'''
#if-Anweisung
wochentag = input("Geben Sie den Wochentag ein: ")

if wochentag == "Freitag":
    print("bald geschaft")

#Moglichkeit 
elif wochentag in ["Sa", "So"]:
    print("juhu") 

#Wenn Bedingung falsch
else: 
    print("Fehler") 
'''

'''
hobby = input("Geben Sie Hobby: ")

if hobby == "zocken":
    print("yeah")

#Wenn Bedingung falsch
else: 
    print("such dir was besseres!") 
'''

'''
#Aufgabe1
wetter = input("Wetter ist: ")

if wetter == "Sonne":
    print("Sonnenbrille einpacken")

elif wetter == "Regen":
    print("Regenschirm einpacken") 

elif wetter == "Schnee":
    print("eine Mutze aufsetyen")        
else: 
    print("Fehler") 
'''


'''
#Aufgabe2

a = input("Bitte geben erste Zahl: ")
b = input("Bitte geben zweite Zahl: ")
c = input("Bitte geben dritte Zahl: ")

if (a > b) and (a > c):
    print("Erste Zahl ist am grossten")
elif (b > a) and (b > c):
    print("Zweite Zahl am grossten")  
elif (c > a) and (c > b):
    print("Dritte Zahl am grossten")  

print("------------------------END-----------------------")
'''


'''
#Aufgabe3

schaltjahre = int(input("Bitte geben Sie Jahr: "))

if schaltjahre % 400 == 0:
    print("Schaltjahr")
elif schaltjahre % 4 == 0 and schaltjahre % 100 != 0:
    print("Schaltjahr")
else:
    print("Fehler, probiren bitte noch mal")          
'''

#Aufgabe4
#Aufgabe5


'''
# random - unsere erste Bibliothek
import random

wochentag = ["mo", "di", "mi"]
heute = random.choice(wochentag)
print(heute)
'''


'''
#Aufgabe1.random

import random

zahl = random.randint(1,20)
print(zahl)
if zahl < 10:
    print("Zahl ist kleine als 10")
elif zahl > 10:
    print("Zahl ist grosser als 10") 
'''      

#Aufgabe4 Schwierige 

#1 Variant
'''
mynumber = list(range(6, 101, 6))
print(mynumber)
'''

'''
#2 Variant
for i in range(1, 101):
    if i % 6 == 0:
        print(i)
    elif i % 8 == 0:
        print(i)   
'''


#Aufgabe5

zahl = int(input("Bitte geben Sie Zahl: "))
zahl_als_string = str(zahl)       #Jetzt wandeln wir die Zahl in einen String um, weil man über den iterieren kann
liste = [int(i) for i in zahl_als_string]       #Als nächstes wollen wir eine Liste mit den einzelnen Ziffern
quersumme = sum(liste)
print(quersumme)








