### WAP to print contents of a directory using os module.

import os

# Select the directory whose content you want to list 
directory_path = '/'

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

print(contents)