



def napeshatat_privetstvie(name):
    """Print Privetstvie"""
    print("Congratulations " + name +  " wish you all the best")
    

def aaaa():
    print("AAAA")

def summa(x, y):
    return x+y 


def factorial(x):
    """Calculate Factorial of number X"""
    otvet = 1
    for i in range(1, x + 1):
        otvet = otvet * i
    return otvet






#--------------------------------------------------------------

print("---------------------")
napeshatat_privetstvie("Denis")
napeshatat_privetstvie("Vasya")
aaaa()

#summa(10, 20)
x = summa (33, 22)
print(x) 


for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))