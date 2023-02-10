from hero import *

myhero = Hero("Vurdalak", 4, "Orc")
mysuperhero = SuperHero("Moisey", 10, "Human", 5)

myhero.show_hero()
mysuperhero.show_hero()

mysuperhero.makemagic()
mysuperhero.show_hero()

mysuperhero.makemagic()
mysuperhero.makemagic()
mysuperhero.show_hero()

# Проверка с двумя андеркорами, так пишем, когда хотим, чтобы не менялась функция, метод 
mysuperhero.__magic = 10 
mysuperhero.show_hero()