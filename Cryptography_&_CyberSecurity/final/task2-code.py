#Switches one character with another in a string by using a replacement list
def switch_char (txt, switchlist):
    toReturn = ""
    
    for i in range(0, len(txt)):
        if txt[i].lower() in switchlist:
            toReturn += switchlist.get(txt[i].lower())
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

list4 = {
    "h" : "e",
    "g" : "t",
    "i" : "n",
    "z" : "a",
    "c" : "i",
    "u" : "s",
    "e" : "o",
    "f" : "d",
    "o" : "h",
    "w" : "d",
    "q" : "u",
    "r" : "c",
    "a" : "m",
    "v" : "p",
    "s" : "y",
    "y" : "s",
    "m" : "d",
    "n" : "g",
}

list5 = {
    "h": "e",
    "g": "t",
    "i": "n",
    "z": "a",
    "l": "s",
    "c": "i",
    "u": "r",
    "e": "o",
    "f": "c",
    "o": "h",
    "w": "u",
    "q": "f",
    "r": "c",
    "a": "y",
    "v": "g",
    "s": "b",
    "y": "z",
    "m": "d",
    "n": "p",
}


solution = {
    "g": "t", 
    "o": "h",
    "h": "e",
    "z": "a",
    "i": "n",
    "m": "d",
    "u": "r",
    "b": "m",
    "e": "o",
    "l": "s",
    "f": "c",
    "q": "f",
    "x": "q",
    "w": "u",
    "a": "y",
    "r": "l",
    "c": "i",
    "s": "b",
    "n": "p",
    "v": "g",
    "t": "x",
    "j": "w",
    "p": "v",
    "y": "z",
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
elif list == "list4":
	print(switch_char(txt, list4))
elif list == "list5":
	print(switch_char(txt, list5))
elif list == "solution":
	print(switch_char(txt, solution))

else:
	print(list, "not a valid list.")
