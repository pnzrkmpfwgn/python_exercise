import re

with open('data.txt',encoding="utf-8") as file:
    data = file.read().rstrip()

new_data = re.sub(r'[0-9]','',data)
new_data=re.sub(r'[^\w]','',new_data)
new_data=new_data.lower()
print(new_data)



# pattern=r'[0-9]'
# new_data = re.sub(pattern, '',data)

# print(new_data)
