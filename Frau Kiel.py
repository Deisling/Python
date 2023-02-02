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



##### AUFGABE5 #####
#Transporte mit Lieferwagen und Lastwagen
print("Aufgabe5")

lieferwagen = int(input("lieferwagen"))
lastwagen = int(input("lastwagen"))
kmLieferwagen = int(input("kmLieferwagen"))
kmLastwagen = int(input("kmLastwagen"))

preisTransport = lieferwagen*kmLieferwagen+lastwagen*kmLastwagen
print("Preis ist", preisTransport)


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



