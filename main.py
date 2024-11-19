import requests
import os 
from bs4 import BeautifulSoup
import urllib
import lxml

def write_file(soup: BeautifulSoup, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

# Define the headers
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "User-Agent": "my-app/0.0.1",
    "Content-Type": "application/json"
}

url = "https://www.1quaidescompetences.fr/coaching/coaching-en-developpement-personnel-coaching-de-vie-nantes-44/"
r = requests.get(url,headers=headers)

if not r.ok:
    print("Request failed with status code:", r.status_code) 
    exit(1)

soup = BeautifulSoup(r.content,"lxml")

path = soup.find('title').text.replace(" ","_")

if  not os.path.exists(path):
    os.mkdir(path)
    os.mkdir(path+"/style")
    os.mkdir(path+"/script")
    os.mkdir(path+"/resources")

write_file(soup,path+"/index.html")