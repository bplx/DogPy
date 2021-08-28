# get dogs

# import stuff and setup stuff lol
import requests
import json
import os
import time

# make variables
dogcount = 1

def getdog(breed, subbreed):

    # dog url
    def decider():
        if breed == "" and subbreed == "":
            print("A")
            return 'https://dog.ceo/api/breeds/image/random'
        elif breed != "" and subbreed == "":
            return 'https://dog.ceo/api/breed/' + breed + '/images/random'
        else:
            return 'https://dog.ceo/api/breed/' + breed + '/' + subbreed + '/images/random'
   
    
    dog = decider()
    print(dog)
    # get request dog

    getdog = requests.get(dog) 
    print(getdog)

    # there was a heap of code here but i removed it


    # print dog
    dogjson = getdog.json()
    
    os.system('clear')
    print('currently viewing: ' + dogjson['message'])

    os.system('feh ' + dogjson['message'])
    return dogcount + 1

def mainloop():
    
    if dogcount == 0:
        print('welcome to dog program. close feh window for new dog prompt')
        getdog()
    
    if dogcount >= 0:
        print('want another dog? [enter] for random dog, breed (type) for a certain breed, [l] to list breeds, [q] to quit. (' + str(dogcount) + ' dog(s) viewed)')
        answer = input()
        
        splitanswer = answer.split(" ")
        
        try:
           breed = splitanswer[0]
           subbreed = splitanswer[1]
        except:
           print()

        try:
            if splitanswer[0] and splitanswer[1]:
                return splitanswer
        except: 
            print()
        
        if splitanswer[0] == "l":
            getdog = requests.get("https://dog.ceo/api/breeds/list/all")
            breedlist = getdog.json()
            breedlistdict = breedlist["message"]
            for i in breedlistdict:
                if breedlistdict[i] == []:
                    print(i)
                else:
                    print(i, "| types:", breedlistdict[i])
            mainloop()
        
        elif splitanswer[0] == "":
            print()
            
        elif splitanswer[0] == "q":
            exit()
        elif len(str(splitanswer[0])) <= 2:
            print(" .                      ")
            print("/!\ input not recognized")
            print("'''                     ")
            time.sleep(1)
            mainloop()
            
        if len(str(splitanswer)) >= 3:
            print()
            return splitanswer

# start program
while True:

    answers = mainloop()
    print("answers", answers)
    try:
        dogcount = getdog(answers[0], answers[1])
    except:
        if answers != None:
            dogcount = getdog(answers[0], "")
        else:
            dogcount = getdog("", "")



