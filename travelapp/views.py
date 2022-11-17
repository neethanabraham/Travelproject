from django.shortcuts import render
from .models import Place
from .models import Person
from django.http import HttpResponse
# Create your views here.

#def demo(request):
  #return  HttpResponse("hello world")

def demo(request):
   obj=Place.objects.all()
   obj1=Person.objects.all()
   #name="Indian"
   return  render(request,"index.html",{'result':obj,'result1':obj1})
#def addition(request):
  # return render(request,"about.html")
#def contact(request):
  #  return HttpResponse("hello I am contact")
#def addition(request):
   #X=int(request.GET['num1'])
   #Y=int(request.GET['num2'])
   #add=X+Y
   #sub=X-Y
   #mul=X*Y
   #div=X/Y

   #return render(request,"result.html",{'sum':add,'dif':sub,'prod':mul,'rem':div})


