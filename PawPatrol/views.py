from django.http import HttpResponse

def signed_in(request):
    text = """<h1>You have sucessfully signed in.</h1>"""
    return HttpResponse(text)
