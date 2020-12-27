from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def works(request):
    return render(request, 'portfolio/works.html')


def about(request):
    return render(request, 'portfolio/about.html')

def iprrelated(request):
    return render(request, 'portfolio/iprrelated.html')


def labour(request):
    return render(request, 'portfolio/labour.html')


def mcaroc(request):
    return render(request, 'portfolio/mca&roc.html')


def others(request):
    return render(request, 'portfolio/others.html')


def sebi(request):
    return render(request, 'portfolio/sebi.html')


def startup(request):
    return render(request, 'portfolio/startup.html')


def taxplanning(request):
    return render(request, 'portfolio/taxplanning.html')