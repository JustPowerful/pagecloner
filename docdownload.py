# install pywebcopy from official github page: https://github.com/rajatomar788/pywebcopy
import os
import requests
import bs4
from pywebcopy import save_webpage 
filename = "data.txt"
with open(filename) as file:
    lines = file.readlines()

foldername=""
for line in lines:
    if(line.startswith("*")):
        foldername = line.replace("*", "").replace("\n", "")
        
        if(not(os.path.exists(foldername))):
            os.mkdir(foldername)
    else:
        currenturl = line.replace("\n", "")

        req = requests.get(currenturl, allow_redirects=False)
        soup = bs4.BeautifulSoup(req.text, features="html.parser")
        try:
            webtitle = soup.find("title").text
        except AttributeError:
            webtitle = "Unnamed please rename it"
        filetitle = "".join(x for x in webtitle if x.isalnum())

        kwargs = {'bypass_robots': True, 'project_name': filetitle}
        try:
            save_webpage(currenturl, "./{}".format(foldername), bypass_robots=True, project_name=filetitle)
        except pywebcopy.exceptions.AccessError:
            print("ERROR BABY")