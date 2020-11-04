from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def bath(request):
    return render(request, 'bath.html', {})

def gardening(request):
    return render(request, 'gardening.html', {})

def household(request):
    return render(request, 'household.html', {})