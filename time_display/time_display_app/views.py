from django.shortcuts import render
from time import gmtime, strftime

def root(request):
    context = {
        "date": strftime("%b %d, %Y %p", gmtime()),
        "time": strftime("%I:%M %p", gmtime())
    }
    return render(request, 'index.html', context)
