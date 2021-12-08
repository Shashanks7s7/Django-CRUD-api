import json
import difflib

data=json.load(open("data/data.json"))
def translate(word):
    word=word.lower()
    if word in data: 
        return data[word]
    elif len( difflib.get_close_matches(word,data.keys()))>0:
       ans= input("Did you mean %s instead? Enter y if yes or n if no. " % difflib.get_close_matches(word,data.keys())[0])
       if ans=='y':
           return data[ difflib.get_close_matches(word,data.keys())[0]]
       elif ans=="n":
           return"The word doesnot exists. Please double cheak it."
    else:
        return "The word doesnot exists. Please double cheak it."
userinput=input("Enter the word:")
answer=translate(userinput)
if type(answer)==list:
    for items in answer:
        print(items)
else:
    print(answer)        