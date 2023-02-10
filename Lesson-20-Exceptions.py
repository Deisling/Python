
import sys 
filename = "Lesson_List.txt"

while True:
    try:
        print("Inside TRY")    
        myfile = open(filename, mode='r', encoding="latin-1")
    except Exception:
        print("Inside EXCEPT")
        print("Error Found!")
        print(sys.exc_info()[1])
        filename = input('Enter Correct file name! :' )
    else:
        print("Insside ELSE")
        print(myfile.read())
        sys.exit()   
         
    
print("==================END==================")        



