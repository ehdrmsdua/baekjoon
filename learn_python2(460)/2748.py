n= int(input())
p=[0,1,1]
for i in range(3,n+1):
    p.append(p[i-1] + p[i-2])
print(p[n])