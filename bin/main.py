# get dogs
# WARNING // INDEV VERSION 0.2

# import stuff and setup stuff lol
import requests
import json
import os
import time

# make variables
dogcount = 1

def getdog():
    global dogcount
    # dog url
    dog = 'https://dog.ceo/api/breeds/image/random'

    # get request dog

    getdog = requests.get(dog) 


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
        print('want another dog? [enter] for yes, [l] to list breeds, [q] to quit. (' + str(dogcount) + ' dog(s) viewed)')
        answer = input()
        if answer == "":
            print()
        elif answer == "q":
            exit()
        else: 
            print(" .                      ")
            print("/!\ input not recognized")
            print("'''                     ")
            time.sleep()
            mainloop()
            
# start program
while True:
    mainloop()
    dogcount = getdog()



