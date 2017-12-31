import os
import time

curDir = os.getcwd()
print(curDir)

#Make Directory
os.mkdir('newDir')
#Rename Directory
os.rename('newDir','newDir2')
#Remove Directory
os.rmdir('newDir2')
