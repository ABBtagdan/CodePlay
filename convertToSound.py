currentDirectory = ""
def handleInput(input):
    global currentDirectory
    stringInput = input

    #stringInput = input("\n Enter a series of integers from 0 to 4.  --->  ")
    #print(" Your chosen is series is as follows: "+ stringInput +"\n")
    """    // The lines above are exclusively used for testing. 
            'stringInput' can receive string from any source.   """

    stringList = list(stringInput)
    audioList = []
    #print(stringList)      #    // Debugging purposes

    for digit in stringList:
        if digit == "0":
            currentDirectory = "./sounds/doo"
        elif digit =="1":
            currentDirectory = "./sounds/ree"
        elif digit =="2":
            currentDirectory = "./sounds/mii"
        elif digit =="3":
            currentDirectory = "./sounds/faa"
        elif digit =="4":
            currentDirectory = "./sounds/sol"
        else:
            print ("oh no") #    // Debugging purposes - Received only upon incorrect input
        audioList.append(currentDirectory)
    
    return audioList

#print(audioList)        #    // Debugging purposes