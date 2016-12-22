from django.shortcuts import render
from .models import User2, Airlines2
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from .forms import LoginForm, SignupForm


def login(request):
    redirect_url = '/index'
    if request.method == 'POST':
        redirect_url = '/index'
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['login'],
                                     password=form.cleaned_data['password'])
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(redirect_url)
            else:
                form.add_error(None, 'invalid login/password')
    else:
        form = LoginForm()
    return render(request, 'auth.html', {'form':form, 'continue': redirect_url})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/index')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form,
                                           'type': 'Registration'})
def index(request):
    airlines = Airlines2.objects.all()
    return render(request, "objects_list.html", {'airlines': airlines})


def flight(request, id):
    data = {
        'flight': {
            'id': id
        }
    }
    return render(request, "object.html", data)