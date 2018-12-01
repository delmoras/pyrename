# pyrename
Recently I had to rename a folder with more than 100 subfolders and more than 14gb of photos .
I chose to use python for this job and wrote a generic script which can handle similar operation in the future.
The script walks through subfolders of the specified folder and rename the file with the wanted extention . 

Future update will check deeper than the first level 

Usage python <path_to_parent_folder> <old_extension> <new_extension>