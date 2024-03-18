from ast import List
import re


def flattener(lists):
    output = []
    for l in lists:
        if type(l) == list:
            print("List found. Recursing.")
            output.extend(flattener(l))
        
        else:
            print("Lowest level list found. Adding", l, "to output.")
            output.append(l)
            

    print("Output in this level: ", output)
    return output
            



# note that all lists need to be passed in a container list
print("final list:", flattener([[1, 2, 3], [4, 5], [6, 7]]))
print("final list:", flattener([[1, 2, 3], "4", [5, 6]]))
# test out additional parameters as necessary
