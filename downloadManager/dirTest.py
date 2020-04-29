# https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
print(os.path.isdir(dir_path))

