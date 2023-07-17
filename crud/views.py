from django.shortcuts import render

# Create your views here.
from django .http import HttpResponse
def function(request):
    return render(request,"crud/index.html")