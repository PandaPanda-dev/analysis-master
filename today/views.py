from bs4 import BeautifulSoup
from django.shortcuts import render

import requests

def index(request):
    return render(request, 'today/index.html')

def show(request):

    url = 'https://p-ken.jp/p-playlanddai1heiwa/bonus'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    ul_tag = soup.find("ul", id="collapse_0")
    a_tags = ul_tag.find_all("a")

    urlList = []
    for a_tag in a_tags:
        urlList.append(a_tag.get("href"))

    return render(request, 'today/show.html')
