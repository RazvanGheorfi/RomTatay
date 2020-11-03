from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def bath(request):
    return render(request, 'bath.html', {})