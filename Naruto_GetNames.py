"""This file will get the list of the shippuden episode names from the wikipedia page"""

import urllib.request

url = r'https://en.wikipedia.org/wiki/List_of_Naruto:_Shippuden_episodes'
response = urllib.request.urlopen(url)
source_code = str(response.read().decode("utf-8"))

start = r'<td class="summary" style="text-align: left;">'
end = r'<br />'

episodeName = []

while (source_code.find(start) != -1):
    temp_start_num = source_code.find(start)
    temp_source_code = source_code[temp_start_num + 47:]
    source_code = source_code[temp_start_num + 47:]
    temp_end_num = temp_source_code.find(end)
    name = temp_source_code[:temp_end_num - 1]
    episodeName.append(name)


def returnEpisodeNames():
    return episodeName

def getName(episode_num):
    """
    :param episode_num: The episode num whose name has ti be given
    :return: The episode number
    """
    episode_list = returnEpisodeNames()
    return episode_list[episode_num-1]

def getStartName(episode_num):
    """
    :param episode_num: the episode number
    :return: StartName of episode in form of SXXEXXX
    """
    seasonList = [32, 53, 71, 88, 112, 143, 151, 175, 196, 221, 242, 275, 295, 320, 348, 361, 372, 393, 413, 479, 500]
    seasonNum = 0
    season = "S"
    for index in range(0, len(seasonList)):
        if episode_num <= seasonList[index]:
            seasonNum = index +1
            break
    if seasonNum<10:
        season = season +"0"+ str(seasonNum)
    else:
        season = season +str(seasonNum)
    episode = "E"
    if episode_num<10:
        episode = episode +"00"+str(episode_num)
    elif episode_num<100:
        episode = episode + "0"+str(episode_num)
    else:
        episode = episode + str(episode_num)
    startName = season+episode
    return  startName

def getLastName(episode_num):
    return getName(episode_num)

def getFullName(episode_num):

    lastName = getLastName(episode_num)
    if '<'in lastName:
        print("Error in getting Last name,Pls add manually\n")
        print(lastName)
        lastName = input()
    fullName = getStartName(episode_num)+" "+ lastName
    return fullName
