from django.shortcuts import render

# Create your views here.

def forloop(request):

    d={'Name':'Sahithi'}
    return render(request,'forloop.html',context=d)
