from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Dummy data

posts = [
    {
        'user': 'Alisha Kavene',
        'title': ' Portfolio Website',
        'content': 'Website review',
        'date_posted':'August 20,2020'
    },
    {
        'user': 'Jane Doe',
        'title': ' Photogallery Website',
        'content': 'Website review',
        'date_posted':'August 20,2020'
    }


]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'all-awwards/base.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account has been created! Now you can Login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'all-awwards/register.html',{'form':form})

@login_required
def profile(request):
    return render(request, 'all-awwards/profile.html')
