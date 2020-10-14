from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient

# Create your views here.

def test(request):
    return HttpResponse("Connection Success")

def main(request):
    return render(request, 'main.html')

def listwithmongo(request):
    data = request.GET.copy()
    with MongoClient('mongodb://127.0.0.1:27017/') as client: # use my ip and sync with datas/worknet.py
        jobdb = client.jobdb
        result = list(jobdb.datalist.find({}))
        data['page_obj'] = result
    return render(request, 'listwithmongo.html', context=data)