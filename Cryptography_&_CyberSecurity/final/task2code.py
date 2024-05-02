#Switches one character with another in a string by using a replacement list
def switch_char(txt, list):
    toReturn = ""
    
    for i in len(txt):
        if txt[i] in list:
            toReturn += list.get(txt[i])
        else:
            toReturn += txt[i]
            
    return toReturn

#Character test lists

list1 = {
    "h" : "e",
    "g" : "t",
    "i" : "a",
    "z" : "o",
    "l" : "n",
    "c" : "i",
    "u" : "s",
    "e" : "h",
    "f" : "r",
    "o" : "l",
    "w" : "d",
    "q" : "u",
    "r" : "c",
    "a" : "m",
    "v" : "p",
}

list2 = {
    "h" : "e",
    "g" : "t",
    "i" : "a",
    "z" : "o",
    "l" : "n",
    "c" : "i",
    "u" : "s",
    "e" : "h",
    "f" : "r",
    "o" : "l",
    "w" : "d",
    "q" : "u",
    "r" : "c",
    "a" : "m",
    "v" : "p",
    "s" : "y",
    "y" : "s",
}

list3 = {
    "h" : "e",
    "g" : "t",
    "i" : "a",
    "z" : "o",
    "l" : "n",
    "c" : "i",
    "u" : "s",
    "e" : "h",
    "f" : "r",
    "o" : "l",
    "w" : "d",
    "q" : "u",
    "r" : "c",
    "a" : "m",
    "v" : "p",
    "s" : "y",
    "y" : "s",
    "m" : "f",
    "n" : "g",
}




#Run the code through terminal with arguments

import sys

if len(sys.argv) != 3:
    print("Usage: python task2code.py <string> <list>")
    sys.exit(1)

txt = sys.argv[1]
list = sys.argv[2]

#If the txt is a text file, read the file and store it in txt
if ".txt" in txt:
    with open(txt, "r") as file:
        txt = file.read()

if list == "list1":
    print(switch_char(txt, list1))
elif list == "list2":
    print(switch_char(txt, list2))
elif list == "list3":
    print(switch_char(txt, list3))