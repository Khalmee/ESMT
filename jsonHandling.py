import json



def createModDotjson(modName, directory): #takes mod folder as directory
    modDotjsonText = json.dumps({'Name': modName, 'Description': "Mod created with ESMT.", 'Version': "1.0.0",'LoadPriority': 0}, indent=4)
    directory+="\\mod.json"
    modDotjson = open(directory, "w")
    modDotjson.write(modDotjsonText)
    modDotjson.close()
    #print(modDotjsonText)


def createEventDotjson(eventName, directory, strategy): #takes audio folder as directory
    modDotjsonText = json.dumps({'EventId': [eventName], 'AudioSelectionStrategy': strategy}, indent=4)
    directory+="\\"+eventName+".json"
    modDotjson = open(directory, "w")
    modDotjson.write(modDotjsonText)
    modDotjson.close()
    #print(modDotjsonText)