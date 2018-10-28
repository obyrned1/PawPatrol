from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Existing user...
            form.save()
            #user gets sent to this URL which is itself at the moment...
            return redirect('login:signed_in')
    else:
        # New user...
        form = UserCreationForm()
    return render(request, 'login/signup.html', {'form': form})

def index(request):
     return render(request, 'login/index.html')

def index2(request):
    text = """<h1>This should be the index page for login... </h1>"""
    return HttpResponse(text)

def signed_in(request):
     return render(request, 'login/profile_page.html')
    
