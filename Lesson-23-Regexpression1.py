



import re

mytext = "Vasya aaaaaaaa 1972,  Kolya - 19727777: Olesya 1981, aaaaaa@intel.com," \
         "bbbbbbbbbb@intel.com, Petya ggggggggg, 1992,cccccccccc@yahoo.com,  " \
         "ddddddddddd@intel.com, vasya@yandex.net, hello hello, Misha #43 1984, " \
         "Vladimir 1977, Irina , 2001,  annnnnnn@intel.com, eeeeeeee@yandex.com," \
         "ooooooooooo@hotmai.gov, gggggggggggg@gov.gov, tututut@giv.hot"

"""
\d   = Any Digit 0-9
\D   = Any non Digit
\w   = Any Alphabet symbol [A-z a-z]
\W   = Any non Alphabet symbol
\s   = breakspace
\S   = non breakspace 

[0-9]{4} = ищет цифры, где 4 подряд, удобно для поиска года рождения 
[A-Z][a-z]+    (+ значит еще сколько угодно)
@\w+\.\w+ = находит все что с эмейлами 

"""


textlooffor = r"@\w+\.\w+"
allresults = re.findall(textlooffor, mytext)

print(allresults)
