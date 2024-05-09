from django.shortcuts import render,redirect

# Create your views here.

def contact_index(request):
    return render(request,'index.html')