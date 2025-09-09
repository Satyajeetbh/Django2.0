from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, World!")

def room(request):
    return HttpResponse("welcome to my room")