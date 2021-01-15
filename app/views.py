from django.shortcuts import render
from .models import Films
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    movie = Films.objects.order_by('?').first()
    return render(request, 'app/index.html', {'movie': movie})

def movielist(request):
    movies = Films.objects.all().order_by('release_year', 'movie')
    page = request.GET.get('page', 1)
    paginator = Paginator(movies, 10)
    try:
        films = paginator.page(page)
    except PageNotAnInteger:
        films = paginator.page(1)
    except EmptyPage:
        films = paginator.page(paginator.num_pages)

    return render(request, 'app/movielist.html', {'films': films})

def search_results(request):
    query= request.GET.get('search')
    queryset = Films.objects.filter(movie__icontains=query)
    return render(request, 'app/search_results.html', {'films': queryset})