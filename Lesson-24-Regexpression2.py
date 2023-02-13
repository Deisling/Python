# Находит в файле все эмейлы кроме intel..., то, что в скобках 
# сайт регулярных выражений  https://regex101.com/, тут можно быстро подобрать 


import re

input_filename = "../dumpfile.txt"
reult_filename = "../results.txt"

inputfile = open(input_filename, mode='r', encoding='Latin-1')
resulfile = open(reult_filename, mode='w', encoding='Latin-1')
mytext = inputfile.read()

lookfor = r"[\w._-]+@(?!intel\.com)[\w._-]+\.[\w.]+"

results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    resulfile.write(item + "\n")


print("Total: " + str(len(results)))

inputfile.close()
resulfile.close()
