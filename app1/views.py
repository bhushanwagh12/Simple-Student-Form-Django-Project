from django.shortcuts import render
from django.http import HttpResponse

import datetime

def wish(request):
    date=datetime.datetime.now()
    var={'insert_date':date}
    return render(request,'wish.html',context=var)




