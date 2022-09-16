
x = int(input())
y = int(input())
z = int(input())
n = int(input())

permu = [ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if 0 <= x and 0 <= y and 0 <= z and (i+j+k != n) ]
print(permu)