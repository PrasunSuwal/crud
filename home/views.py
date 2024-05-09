from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def index(request):
    staffs = Staffs.objects.all()
    if request.method == "POST":
        #data = request.POST
        name = request.POST.get("name")
        email= request.POST.get("email")
        phone= request.POST.get("phone")
        address= request.POST.get("address")
   
        Staffs.objects.create(name=name, email=email, phone=phone, address=address)
        return redirect("/",{'staffs': staffs})
   
    return render(request, 'index.html',{'staffs':staffs})

def edit_staff(request,staff_id):
    if request.method == 'POST':
        staff = get_object_or_404(Staffs, pk=staff_id)
        staff.name = request.POST.get('name')
        staff.email = request.POST.get('email')
        staff.phone = request.POST.get('phone')
        staff.address = request.POST.get('address')
        staff.save()
        
    return redirect('index')
   
def delete_staff(request,staff_id):
    staff = get_object_or_404(Staffs, pk=staff_id)
    staff.delete()
    return redirect('index')

            

