from django.shortcuts import render
import requests
# Create your views here.
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from requests_html import HTMLSession
from urllib.parse import urlparse
from django.template.response import TemplateResponse


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
def url_search(request):
    url = request.GET.get("domain")
    urls = []
    try:
        for new_url in additionURL(url):
            urls.append(new_url)
    except:
        pass
    url += "/*"
    req = requests.get("https://index.commoncrawl.org/CC-MAIN-2018-26-index?output=json&fl=url&url=" + url)
    for i in req.text.split("\n"):
        try:
            urls.append(json.loads(i)["url"])
        except:
            pass
    return HttpResponse("\n".join(list(set(urls))), content_type="text/plain")


@csrf_exempt
def domain_search(request):
    domain = request.GET.get("domain")
    if not domain:
        return HttpResponse("error")
    req = requests.get("https://index.commoncrawl.org/CC-MAIN-2018-26-index?output=json&fl=url&url=*." + domain)
    domains = []
    for i in req.text.split('\n'):
        try:
            i = urlparse(json.loads(i)["url"]).netloc
        except:
            pass
        domains.append(i)
    domains = list(filter(lambda i: len(i) > 1, list(set(domains))))
    return HttpResponse("\n".join(domains), content_type="text/plain")


@csrf_exempt
def index(request):
    return TemplateResponse(request, "index.html")
