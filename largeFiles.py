# python3
# Program finds files of >100MB in a user-specified folder and prints them to the screen.

import os

# Prompt user for folder.
print('Please enter the folder to be searched, e.g., C:\Windows\System32: ')
searchFolder = os.path.normpath(input())

# Walk the directory tree.
for folderName, subfolders, filenames in os.walk(searchFolder):
    for filename in filenames:
        absFilename = os.path.join(folderName, filename)
        if os.path.getsize(absFilename) > 100000000:
            print(absFilename)
