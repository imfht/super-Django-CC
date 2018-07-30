from django.shortcuts import render
import requests
# Create your views here.
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from requests_html import HTMLSession
from urllib.parse import urlparse


def additionURL(url):
    if "http" not in url:
        url = "http://" + url
    session = HTMLSession()
    r = session.get(url, timeout=3)
    _ = []
    netloc = urlparse(url).netloc
    for i in r.html.absolute_links:
        if netloc == urlparse(i).netloc:
            _.append(i)
    return _


@csrf_exempt
def index(request):
    url = request.GET.get("domain")
    if not url:
        return HttpResponse("""
            <!DOCTYPE html><html lang="en"><head><style>.center{width:auto;display:table;margin-left:auto;margin-right:auto}</style><meta charset="UTF-8"><link href="https://cdn.bootcss.com/bootswatch/4.1.1/yeti/bootstrap.min.css" rel="stylesheet"><title>Hi, Hacker.</title></head><body style="text-align:center"><h1>Input Domain</h1><h2>Get Urls in this domain</h2><div class="center"><form class="form-inline"><input class="form-control mr-sm-2" type="text" placeholder="input domain here" name="domain"> <button class="btn btn-secondary my-2 my-sm-0" type="submit">Search</button></form></div></body></html>""")
    urls = []
    for new_url in additionURL(url):
        urls.append(new_url)
    url += "/*"
    req = requests.get("https://index.commoncrawl.org/CC-MAIN-2018-26-index?output=json&url=" + url)
    print(url)
    for i in req.text.split("\n"):
        try:
            urls.append(json.loads(i)["url"])
        except:
            pass
    return HttpResponse("\n".join(list(set(urls))), content_type="text/plain")
