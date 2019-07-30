from django.shortcuts import render

from django.http import HttpResponse
import datetime
def time(request):
    time=datetime.datetime.now()
    t='<h1> Current DATE and TIME :'+str(time)+'</h1>'
    return HttpResponse(t)
