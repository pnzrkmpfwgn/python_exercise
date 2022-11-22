phonebook=[
	{
		"person":("Tansel","Sarıhan"),
		"phone":{"mobile":"1234567890","home":"1234567890"},
		"organization":"EMU"

	},
	{
		"person":("Emre","Yıldız"),
		"phone":{"mobile":"1234567890","home":None},
		"organization":"EMU"
	}
	]
def isEmpty(phonebook):
	for element in phonebook:
		if element:
			return True
		else:
			return False
is_phonebook_empty = isEmpty(phonebook) # returns true as of now

#print(is_phonebook_empty)

#print(phonebook[1+0]["person"][0])

def addNew(name,surname,mobile,home,organization):
	phonebook[len(phonebook)+1]["person"][0] = name
	phonebook[len(phonebook)+1]["person"][1] = surname
	phonebook[len(phonebook)+1]["phone"][0] = mobile
	phonebook[len(phonebook)+1]["phone"][1] = home
	phonebook[len(phonebook)+1]["organization"]= organization

def searchRec(name=None,surname=None,mobile=None,home=None):
	if(name!=None and surname != None):
		name = list(filter(lambda phonebook: phonebook['person'][0] == name, phonebook))
		surname = list(filter(lambda phonebook: phonebook['person'][1] == surname, phonebook))
		print(name)
		
	elif(mobile !=None):
		mobile = list(filter(lambda phonebook: phonebook['phone']["mobile"] == mobile, phonebook))
		print(mobile)
		
	elif(home != None):
		home = list(filter(lambda phonebook: phonebook['phone']["home"] == home, phonebook))
		print(home)
		

def delRec(name=None,surname=None,mobile=None,home=None):
	i = 0
	while(i < len(phonebook)):
		if(phonebook[i]["person"][0]== name and phonebook[i]["person"][1]==surname):
			phonebook.pop(i)
		elif(phonebook[i]["phone"]["home"] == home or phonebook[i]["phone"]["mobile"]==mobile):
			phonebook.pop(i)
		i = i+1
	
def updateRec(name=None,surname=None,mobile=None,home=None,updatedName=None,updatedSurname=None,updatedMobile=None,updatedHome=None):
	i = 0
	indexOfUpdated = 0
	while(i < len(phonebook)):
		if(phonebook[i]["person"][0]== name and phonebook[i]["person"][1]==surname):
			indexOfUpdated = i
			break;
		elif (phonebook[i]["phone"]["home"] == home or phonebook[i]["phone"]["mobile"]==mobile):
			indexOfUpdated = i
			break;
		i = i + 1
	if(name != None):
		phonebook.update(phonebook[updatedHome]["person"][0]=name) 
delRec("Emre","Yıldız")
print(phonebook)


