import random
z=[]
for i in range(0,50):
    die=random.randrange(1,100)
    z.append(die)
print(z)
a=int(input("plase write a number"))
print("it is on list",z.index(a))