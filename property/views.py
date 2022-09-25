from email.mime import image
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Image, Location, Property
from django.core.paginator import Paginator
# Create your views here.


def search(request):
    range = request.GET.get('range', None)
    query = request.GET.get('search', '')
    sorting = request.GET.get('sorting', None)
    curr_page = request.GET.get('page', 1)
    if sorting == 'htl':
        sorting = '-'
    else:
        sorting = ''

    try:
        range = int(range)
    except:
        range = 0

    res = Property.objects.filter(location__name__icontains=query, price__gt=int(
        range)).order_by(f'{sorting}price')
    # print(res)
    card = []
    for property in res.values():
        img = Image.objects.filter(property__id=property['id'])[:1]
        property['image'] = str(img[0])
        card.append(property)

    p = Paginator(card, 3)
    page = p.get_page(int(curr_page))
    return render(request, 'index.html', content_type="text/html", context={'properties': page.object_list,'page':page,'paginator': p})


def home(request):
    res = Property.objects.all()

    card = []
    for property in res.values():
        img = Image.objects.filter(property__id=property['id'])[:1]
        property['image'] = str(img[0])
        card.append(property)
    p = Paginator(card, 3)
    # print(p.object_list)
    for i in p.page_range:
        print("emon")
    page = p.page(1)
    return render(request, 'index.html', content_type="text/html", context={'properties': page.object_list, 'paginator': p, 'page': page})
