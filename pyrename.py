import os
import sys 

#specify arguments that we request from the user
rootdir = sys.argv[1]
oldExt  = sys.argv[2]
newExt  = sys.argv[3]

#check if total arguments are 4 in number which means user has completed everything that we need
total = len(sys.argv)

if total == 4:        
    #walk through the subfolders of the folder that we specified
    for root, subFolders, files in os.walk(rootdir):
        for folder in subFolders:
            print('Entering folder '+folder+'... \n')
            subdir = os.path.join(rootdir,folder)
            print(subdir)
            subFiles = os.listdir(subdir)
            for subFile in subFiles:
                #check if file has the specified old extention
                if subFile.endswith("."+oldExt):                    
                    pre, ext = os.path.splitext(subFile)
                    oldFile = str(subdir+'/'+subFile)
                    newFile = str(subdir+'/'+pre + '.'+newExt)                
                    print('OLD FILE : '+oldFile+'\n')
                    print('NEW FILE : '+newFile)
                    #proceed with the rename of the file
                    os.rename(oldFile,newFile)
                    print(subFile+'\n')            
else:
    print('Usage python <path_to_parent_folder> <old_extension> <new_extension>') 
