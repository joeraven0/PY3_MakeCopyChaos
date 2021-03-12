#Copy data from folder of choice to a chaos structure. Avoid running on system disk ;)
#Joakim Ringstad 2021-03-12

import os, shutil, time, random

counter = 0

#Select folder from where to copy files
fromFolder = "G:/temp/"
#Set destination folder where files will be copied
toFolder = "G:/"


##NOTHING IMPORTANT, NO NEED TO CHANGE BELOW THIS LINE##
folderIncrementor = 0
chaosIncrementor = 0

while True:
    
    #Used to create a strange folder name
    folderIncrementor = folderIncrementor+random.randint(1,20) * random.randint(1,12345)
    #Find all files to copy from folder
    filenames = os.listdir(fromFolder)
    #Again strange folder name are being created
    toFolder0 = toFolder+str(folderIncrementor)+"veryImportantFiles!"+str(random.randint(1,101))+"."+chr(random.randint(1,9999))
    
    try:
        #Create wierd folder name and tell user
        os.mkdir(toFolder0)
        print("Preparing new folder: "+ toFolder0)
        file = ""
        for filename in filenames:
            
            #Only to reduce amount of prints in console. Show when copying every 100th file.
            if random.randint(0,100)>99:
                print(toFolder0+"/"+filename)
                
            #Copy the file to the new strange folder name    
            shutil.copy(fromFolder+filename,toFolder0)
            file = filename
            
            chaosIncrementor = chaosIncrementor + 1
        shutil.copy(fromFolder+file,toFolder0+chaosIncrementor)
        print("Copied files to folder: "+toFolder0)
        print("Created chaosIncrementor file: "+toFolder0+str(chaosIncrementor))
        folderIncrementor = folderIncrementor + 1
    #Exception if folder can't be created or disk is full. Need to be stopped manually...
    except:
        #Show only each 50th error since program will interate too fast for you to read everything anyhow
        if folderIncrementor % 50 == 0:
            print("Error: Folder " +toFolder)
        folderIncrementor = folderIncrementor + 1
        #If cycled over 1 million times, a delay will let the computer relax. Typically if running over night and disk should have been full.
        if folderIncrementor>1000000:
            time.sleep(5)
