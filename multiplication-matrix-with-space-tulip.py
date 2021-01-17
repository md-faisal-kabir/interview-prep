# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n = 13
a = [1,2,3,4,5,6,7,8,9,10,11,12]

array =[]


#n 
for i in range(1,n):
    array.append([x*i for x in a])

# 1 2 3 4 

maxnumber = array[-1]
print(maxnumber)

    
for item in array:
    s = ""
    for i in range(0,n-1):
        space = len(str(maxnumber[i]))
        current = len(str(item[i]))
        
        
        if(space-current == 0):
            s +=  str(item[i]) + " "
        else:
            s +=  str(item[i]) + " "*(space-current+1)
    print(s)
    
# 1  2  3  4
# 2  4  6  8
# 12 13 14 15