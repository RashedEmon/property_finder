from django.shortcuts import render

# Create your views here.
def home(request):
    print('home page hit')
    return render(request,'index.html')