from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Python")
    
def home(request):
    return HttpResponse("This is home page")

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is contact page")

def services(request):
    return HttpResponse("This is services page")