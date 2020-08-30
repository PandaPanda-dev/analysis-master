from bs4 import BeautifulSoup
from django.shortcuts import render

import os
import requests

def index(request):
    return render(request, 'today/index.html')

def show(request):

    url = 'https://p-ken.jp/p-playlanddai1heiwa/bonus'

    os.environ['NO_PROXY'] = 'localhost,127.0.0.1,localaddress,.localdomain.com,/var/run/docker.sock,p-ken.jp'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    ul_tag = soup.find("ul", id="collapse_0")
    a_tags = ul_tag.find_all("a")

    urlList = []
    for a_tag in a_tags:
        urlList.append(a_tag.get("href"))

    return render(request, 'today/show.html')
