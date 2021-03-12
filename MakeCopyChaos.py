#Copy data from folder of choice to a chaos structure. Avoid running on system disk ;)
#Joakim Ringstad 2021-03-12

import os, shutil, time, random

counter = 0

fromFolder = "G:/temp/"
toFolder = "G:/"

folderIncrementor = 0
chaosIncrementor = 0

while True:
    
    folderIncrementor = folderIncrementor+random.randint(1,20) * random.randint(1,12345)
    filenames = os.listdir(fromFolder)
    toFolder0 = toFolder+str(folderIncrementor)+"veryImportantFiles!"+str(random.randint(1,101))+"."+chr(random.randint(1,9999))
    
    try:
        os.mkdir(toFolder0)
        print("Preparing new folder: "+ toFolder0)
        file = ""
        for filename in filenames:
            
            if random.randint(0,100)>99:
                print(toFolder0+"/"+filename)
            shutil.copy(fromFolder+filename,toFolder0)
            file = filename
            
            chaosIncrementor = chaosIncrementor + 1
        shutil.copy(fromFolder+file,toFolder0+chaosIncrementor)
        print("Copied files to folder: "+toFolder0)
        print("Created chaosIncrementor file: "+toFolder0+str(chaosIncrementor))
        folderIncrementor = folderIncrementor + 1
    except:
        if folderIncrementor % 50 == 0:
            print("Error: Folder " +toFolder)
        folderIncrementor = folderIncrementor + 1
        if folderIncrementor>1000000:
            time.sleep(5)
