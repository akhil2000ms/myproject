from django.shortcuts import redirect, render
from testapp1.models import Registration

# Create your views here.
def homePageView(request):
    return render(request,'home.html',{"test":"Hello world"})

def loginView(request):
   
    if request.method=='POST':
        user=request.POST['usernamee']
        passwrd=request.POST['passwordd']
        data=Registration.objects.filter(Username=user)
        print(data.values())
        return redirect("homePageView")
    else:
        return render(request,'login.html')

def registerView(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        phone=request.POST['phone']
        reg=Registration(Username=username,Password=password,Email=email,phone= phone)
        reg.save()
        return redirect('login')
    else: 
        return render(request,'register.html')

