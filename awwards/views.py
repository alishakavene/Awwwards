from django.shortcuts import render
from django.http  import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def welcome(request):
    return render(request, 'all-awwards/base.html')

def register(request):
    form = UserCreationForm()
    return render(request,'all-awwards/register.html',{'form':form})
