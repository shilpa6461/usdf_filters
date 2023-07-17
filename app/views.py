from django.shortcuts import render

# Create your views here.

def usdf(request):
    d={'data':'hAI hARShAD hOw ARe you'}
    return render(request,'usdf.html',d)
