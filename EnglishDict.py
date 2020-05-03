import json
import random
f=open("D:\original.json",'r')
data=json.load(f)
def find(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.lower() in data:
        return data[word.lower()]
    else:
        return "Word not Found in Dictionary"
reply="y"
while reply =='y':
    word=input('Type word to search')
    output=find(word)
    print(word,end='')
    if type(output)== list:
        for item in output:
            print(":-",item)
    else:
        print(":-",output)
    reply=input("To search again press 'y' Press any other key to terminate")
print("Thank you for Using")


    
