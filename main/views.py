from django.contrib.auth import login 
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import SignUpForm


def index(request):
    return render(request, 'main/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return HttpResponseRedirect(reverse(index))
    else:
        form = SignUpForm()
    
    return render(request, 'main/signup.html', {
        'form': form,
    })