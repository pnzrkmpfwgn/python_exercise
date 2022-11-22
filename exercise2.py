i = 0
x=''
y='*'
while i < 6:
    print(x)
    i= i + 1
    x = y + x
i=0
print("\n")
while i < 6:
    x=x[:0] + x[1:]
    print(x)
    i=i+1