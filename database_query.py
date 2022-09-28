from numbers import Number
import numbers
from re import X
import string


n = int(input())
database = []
i = 0 

def average_output(ls_nos) :
    if type(ls_nos) == list :
        sum = 0
        for x in ls_nos :
            if isinstance(x, Number) :
                sum = sum + x
            else :
                print("Function requires a list containing number objects")
        average = sum / len(ls_nos)
    else :
        print("Function takes a list as an input argument")
    #return float("{:.2f}".format(average))
    return average


while 2 <= n <= 10 and i < n :
    getinput = input().split()
    #print(getinput)
    if 0 <= int(getinput[1]) <= 100 and 0 <= int(getinput[2]) <= 100 and 0 <= int(getinput[3]) <= 100 :
        database.append([str(getinput[0]), list(map( int, [getinput[1],getinput[2],getinput[3]] ))])
        print(database)
    del getinput
    i += 1

name_query = str(input())

for x in len(database) :
    for y in (database[x]) :
        
