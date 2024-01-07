from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    pages = []
    with open('./data-398-2018-08-30.csv', encoding='UTF-8') as file:
        inf = csv.reader(file)
        for line in inf:
            if line[1] != 'Name' or line[4] != 'Street' or line[6] != 'District':
                pages.append({'Name': line[1], 'Street': line[4], 'District': line[6]})

    quant_line = Paginator(pages, 10)
    current_page = request.GET.get('page', 1)
    page = quant_line.get_page(current_page)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
