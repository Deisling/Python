import sys
import os

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "/?":
        print("Help Requested")
        print("Usage of this program is python.exe bla bla bla")
    print ("Argumnet entered: " + str(sys.argv[1:]))
else:
    print("Arguments NOT PROVIDED")

os.system("dir > text.txt")
os.mkdir("my dir")
sys.exit()

    