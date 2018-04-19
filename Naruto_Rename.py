import os
import Naruto_GetNames as ns
import sys

#This is a new file to rename all the files for specific folder

#This is specific for Season 2 folder
def show_percentage(x):
    """
    Just a function tio show the percentage x which can be changes accordingly.
    :param x: The perocentage to be displayed type
    :return: None
    """
    sys.stdout.flush()
    sys.stdout.write("\rPecentage Completed: %f" %x)

def getNumberFromName(s):
    num = ""
    for x in s:
        if x.isdigit():
            num = num + x
    return int(num[:3])

if __name__ == "__main__":
    total_files = len(list(os.listdir('.')))
    counter =1
    for file in os.listdir('.'):
        try:
            extension = file[-4:]
            if extension == r'.mkv':
                episode_no = getNumberFromName(file)
                os.rename(file, ns.getFullName(int(episode_no)) + extension)
            show_percentage(counter*100 / total_files)
            counter += 1
        except Exception as e:
            print(e)
