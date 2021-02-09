# A program to parse through a directory of files
# Search through files and delete a specific string

import os


def parseDir(dir_path):
    for subdir, dirs, files in os.walk(dir_path):
        for filename in files:
            filepath = subdir + os.path.sep + filename
            print(filepath)

if __name__ == '__main__':
    check = input("Are you in the directory that you want to parse? [y/n]: ")
    if (check == 'y'):
        dir_path = os.path.abspath(os.getcwd())
    elif (check == 'n'):
        dir_path = input("Enter the path to the directory: ")
    else:
        print('Exiting: User failed to make up mind')
    print(dir_path)
    parseDir(dir_path)
