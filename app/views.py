from django.shortcuts import render

# Create your views here.
def popovers(request):
    return render(request,'Popovers.html')