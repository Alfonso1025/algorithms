from cgitb import text
#from bs4 import BeautifulSoup
import urllib
import requests
import re

def get_image_Ofperson(name):
    person_url=[]
    urlPage='http://en.wikipedia.org/wiki/'+name
    page=requests.get(urlPage).text
    print(page)

get_image_Ofperson('elon musk')


