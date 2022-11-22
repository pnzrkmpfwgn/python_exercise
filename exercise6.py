def f1(i,j):
    if i==0 :
        return 'A'
    if j==0 or j==8 :
        return'A'
    if i==1 and j in range(1,8) :
        return'B'
    if j==1 or j==7 :
         return'B'
    if i==2 and j>=2 and j<=6 :
        return'3'
    if j==2 or j==6 :
         return'3'   
    if i==3 and j>=3 and j<=5 :
        return'4'
    if j==3 or j==5 :
         return'4'   
 
    else: 
        return'E'



for i in range(5):
    
    
    for j in range(9):
        print(f1(i,j), end=' ')
    print()