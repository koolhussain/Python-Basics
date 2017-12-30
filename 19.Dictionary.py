exDict = {'Jack':[75,'White'],'Bob':[22,'brown'],'Ahmad':[23,'Blue'],'Kevin':[17,'Black']}

print(exDict)

print(exDict['Jack'])
#Adding New Key-value pair
exDict['Tim'] = 54

print(exDict)
#Modifiy Old Key-Value pair
exDict['Tim'] = 15

print(exDict)
#Deleteing a Key-Value Pair
del exDict['Tim']

print(exDict)
#REfernceing values of a key with a list
print(exDict['Jack'][1])
