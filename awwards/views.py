from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def home(request):
    return render(request, 'all-awwards/base.html')

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
