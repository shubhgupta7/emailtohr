from django.shortcuts import render
from django.http import HttpResponse
import datetime
def index(request):
    return HttpResponse(f"Hello Sir you're checking the server at : {datetime.datetime.now()} ",)


# Create your views here.
