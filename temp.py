import random
dict = [0,0,0]
n = 1000000
for i in range(n):
    dict[int(random.random() * 3)] += 1

for i,a in enumerate(dict):
    a /= n
    dict[i] = a*100
print(f"{dict}%")
