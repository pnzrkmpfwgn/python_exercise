from difflib import SequenceMatcher

def similar(a,b):
        return SequenceMatcher(None,a,b).ratio()
x=similar("Hello World","World Hello")
print(x)