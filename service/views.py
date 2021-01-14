from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def inquiry(request):
    return render(request, 'inquiry.html')


def contactus(request):
    return render(request, 'contactus.html')


def termsofservice(request):
    return render(request, 'termsofservice.html')


def result(request):
    return render(request, 'result.html')

