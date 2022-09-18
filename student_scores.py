from cmath import inf
from numbers import Number
import numbers

n = int(input())
names, scores, data = [],[],[]
for x in range(n) if 2 <= n <= 5 else 0 :
    name = input()
    score = float(input())
    scores.append(score)
    data.append([name,score])

ls,sls= 1000,1000

for i in range(len(data)) :
    #print(i)
    for j in range(len(data[i])) :
        #print(j)
        if isinstance(data[i][j], Number) :
            if data[i][j] < ls :
                sls = ls 
                ls = data[i][j]
            elif (data[i][j] < sls and data[i][j] != ls) :
                sls = data[i][j] 
            if i == len(data)-1 and j == len(data[i])-1 :
                desired_score = sls
                #print(ls,sls)

for i in range(len(data)):
    for j in range(len(data[i])) :
        names.append(data[i][j-1]) if isinstance(data[i][j], Number) and data[i][j] == sls else 1
        names.sort()

for x in names:
    print(x)
