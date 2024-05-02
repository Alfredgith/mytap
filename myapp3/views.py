from django.shortcuts import render,redirect
from .models import cas
from .forms import mycas

def rap(request):
    pop=mycas()
    if request.method=='POST':
       pop=mycas(request.POST)
       if pop.is_valid():
           pop.save()
           return redirect('/pass')
       
    else:
        pop=mycas
        pop1=cas.objects.all()
        return render(request,'index.html',{'pop':pop,'pop1':pop1})


