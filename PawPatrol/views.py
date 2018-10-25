from django.http import HttpResponse

def about(request):
    return HttpResponse('about')

def signup(request):
    return HttpResponse('signup')
