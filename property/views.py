from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Max, Min
from urllib.parse import urlencode


from .models import Image, Property

# Create your views here.

# handle request for search query and return search result.


def search(request):
    range = request.GET.get('range', "")
    query = request.GET.get('search', "")
    sorting = request.GET.get('sorting', None)
    curr_page = request.GET.get('page', 1)

    params = {
        'query': query,
        'sorting': sorting
    }

    # print(request.GET)

    tempQuery = request.GET.copy()
    try:
        del tempQuery['page']
    except Exception as e:
        print(e)

    fullPath = '/search/?'
    fullPath += urlencode(tempQuery)
    # check sorting is passed if passed then process the sorting value
    if sorting and sorting == 'htl':
        sorting = '-price'
    elif sorting and sorting == 'lth':
        sorting = 'price'
    else:
        sorting = None

    # get maximum and minimum value from database
    price_range = Property.objects.aggregate(Min('price'), Max('price'))

    # if range is a number value then range will proceed otherwise range will initialize with default value 0
    try:
        range = int(range)
    except:
        range = price_range.price_range['price__min']-1

    params['range'] = range

    if sorting:
        res = Property.objects.filter(location__name__icontains=query, price__gt=int(
            range)).order_by(sorting)
    else:
        res = Property.objects.filter(location__name__icontains=query, price__gt=int(
            range))

    card = []
    for property in res.values():

        try:
            img = Image.objects.filter(property__id=property['id'])[:1]
            property['image'] = str(img[0])
            card.append(property)
        except Exception as e:
            print(e)

    p = Paginator(card, 3)
    page = p.page(int(curr_page))
    return render(request, 'pages/search.html', content_type="text/html", context={'page': page, 'price_range': price_range, 'full_path': fullPath, 'params': params})

# handle request for home page


def home(request):
    curr_page = request.GET.get('page', 1)
    price_range = Property.objects.aggregate(Min('price'), Max('price'))
    res = Property.objects.all()

    card = []
    # iterate through all properties
    for property in res.values():
        try:
            # get a image associated with the property
            img = Image.objects.filter(property__id=property['id'])[:1]
            property['image'] = str(img[0])
            card.append(property)
        except Exception as e:
            print(e)
    p = Paginator(card, 3)
    page = p.get_page(int(curr_page))
    return render(request, 'pages/index.html', content_type="text/html", context={'page': page, 'price_range': price_range})
