from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Location, Property
# Create your views here.
def search(request):
    range = request.GET.get('range',None)
    query = request.GET.get('search',None)
    sorting = request.GET.get('sorting',None)

    if sorting == 'htl':
        sorting = '-'
    else:
        sorting = ''
    
    res=Property.objects.filter(location__name__icontains=query, price__gt=int(range)).order_by(f'{sorting}price')
    for property in res.values():
        print(property)
    print(res)
    return render(request,'index.html',content_type="text/html",context={'properties':res})


def home(request):
    res=Property.objects.all()
    return render(request,'index.html',content_type="text/html",context={'properties':res})