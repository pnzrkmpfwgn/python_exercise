# a=[10,30,2,5,9,6]

# def odd(x):
#     return x%2!=0

# result=list(filter(odd,a)) #if odd is true among a the satisfied number will be returned

# result = [item for item in a if odd(item)]

# result = list(filter(lambda x:x%2!=0,a))

# result=list(map(lambda x:x**2,a))

# for value in(x**2 for x in a if x%2!=0):
#    print(value,end=' ')

# result = list(map(lambda x:x**2,filter(lambda x:x%2!=0,a)))

#print(result)

# a=[[1,2,3],[10,55,66]]

# for i in a:
#    print("[",end="")
#     for k in i:
#        print(k," ",end="") 
#        print("]",end="")
# print("\n")

#print(result)

#import numpy as np
#import random
#import seaborn as sns
#import matplotlib.pyplot as plt

#rolls = [random.randrange(1,7) for i in range(1,600)]
#values,freqs=np.unique(rolls,return_counts=True)

#print(values,end=' ')
#print(freqs,end=' ')

#sns.set_style('darkgrid')
#axes=sns.barplot(x=values,y=freqs,palette='dark')
#axes.set_title='CMPE424'
#plt.show()

#country_codes = {'Finland':'fi',"South Africa":'za'}

#country_codes.clear()

#print(country_codes)

#for i,j in country_codes.items():
    #print(f'The code of {i} is {j}')

#roman_numbs = {'I':1,'II':2,'IV':4,'V':5,'X':100}

#roman_numbs['X']=10

#print(roman_numbs['X'])

#roman_numbs['L']=50

#del roman_numbs['II']

#print(roman_numbs)

#print('II' in roman_numbs)

#roman_numbs.update({'C':100}) #this changes current values so it doesn't add new elements

#for i in roman_numbs.keys():
    #print(i,end=' ')

#for i in roman_numbs.values():
    #print(i,end=' ')

#grades = {'Ali':[50,90],'John':[99,,60,88]} Ali missed midterm but John entered, the inconcistency of the data won't effect the calculations

#g2={k:sum(v)/len(v) for k,v in grades.items()}

#print(g2)
