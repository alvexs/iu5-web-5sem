from django.shortcuts import render
from .models import User2, Airlines2
from django.http import HttpResponse

def index(request):
    #posts = []
    #for i in range(10):
    #    posts.append({ 'header':'header ' + str(i), 'text': ( ' text ' + str(i) ) * 20, 'id': i })
    airlines = Airlines2.objects.all()
    return render(request, "objects_list.html", {'airlines': airlines})


def flight(request, id):
    data = {
        'flight': {
            'id': id
        }
    }
    return render(request, "object.html", data)