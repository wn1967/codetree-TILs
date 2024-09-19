a= input()
b = int(a,2)
c = b*17
d = bin(c)

result = []
for i in range(2,len(d)):
    result.append(d[i])
    aa = ''.join(result)
print(aa)