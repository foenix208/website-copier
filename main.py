import requests
import os 
from bs4 import BeautifulSoup
import lxml

def ft_write(soup: BeautifulSoup, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

def ft_requests(url):

    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "User-Agent": "my-app/0.0.1",
        "Content-Type": "application/json"
    }
    r = requests.get(url,headers=headers)
    if not r.ok:
        print("Request failed with status code:", r.status_code) 
        exit(1)

    return BeautifulSoup(r.content,"lxml")

def ft_all_link(url = None,soup = None):
    link = []
    if url != None:
        soup = ft_requests(url)
    a = soup.find_all("a")

    for i in a:
        link.append(i["href"])
        #print(i["href"])
    return link

url = "https://www.1quaidescompetences.fr"
dommaine ="www.1quaidescompetences.fr"

path_name = "Site_copie"

if  not os.path.exists(path_name):
    os.mkdir(path_name)

soup = ft_requests(url)

ft_write(soup,path_name+"/index.html")
