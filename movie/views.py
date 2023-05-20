from django.shortcuts import render, redirect
from .models import movie as movies
from .models import *
from django.http import JsonResponse
from django.core.mail import send_mail
import smtplib
from django.conf import settings
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    film = movies.objects.filter(session__name="Latest Movies")
    films = movies.objects.all().order_by('-id')[0:9]
    Serie = movies.objects.filter(session__name="Web-series")

    context = {
        'film': film,
        'films': films,
        'Serie': Serie,

    }
    return render(request, "home.html", context)


def moviedetail(request, id):
    film = movies.objects.get(id=id)
    data1 = media.objects.filter(movie_id=film)
    data2 = data1.count()

    context = {

        'film': film,
        'data1': data1,
        'data2': data2,
    }
    return render(request, "moviesingle.html", context)


def movie(request):
    rate_descid = request.GET.get('rating_desc')
    rate_ascid = request.GET.get('rating_asc')
    date_descid = request.GET.get('date_desc')
    date_ascid = request.GET.get('date_asc')

    if rate_descid:
        film = movies.objects.filter(session__name="Latest Movies").order_by('IMDB_rating')
        data = film.count()
    elif rate_ascid:
        film = movies.objects.filter(session__name="Latest Movies").order_by('-IMDB_rating')
        data = film.count()
    elif date_descid:
        film = movies.objects.filter(session__name="Latest Movies").order_by('Releaseyear')
        data = film.count()
    elif date_ascid:
        film = movies.objects.filter(session__name="Latest Movies").order_by('-Releaseyear')
        data = film.count()
    else:
        film = movies.objects.filter(session__name="Latest Movies")
    data = film.count()

    paginator = Paginator(film, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_pages = paginator.num_pages

    context = {

        'film': film,
        'data': data,
        'page_obj': page_obj,
        'total_pages': total_pages

    }
    return render(request, "moviegridfw.html", context)


def search(request):
    if request.GET:

        query = request.GET['query']
        if query:
            film = movies.objects.filter(name__icontains=query)
            data = film.count()
        context = {

            'film': film,
            'data': data

        }
        return render(request, "search.html", context)


def Series(request):
    Serie = movies.objects.filter(session__name__icontains="Web-series")
    data = Serie.count()
    rate_descid = request.GET.get('rating_desc')
    rate_ascid = request.GET.get('rating_asc')
    date_descid = request.GET.get('date_desc')
    date_ascid = request.GET.get('date_asc')

    if rate_descid:
        Serie = movies.objects.filter(session__name__icontains="Web-series").order_by('IMDB_rating')
        data = Serie.count()
    elif rate_ascid:
        Serie = movies.objects.filter(session__name__icontains="Web-series").order_by('-IMDB_rating')
        data = Serie.count()
    elif date_descid:
        Serie = movies.objects.filter(session__name__icontains="Web-series").order_by('Releaseyear')
        data = Serie.count()
    elif date_ascid:
        Serie = movies.objects.filter(session__name__icontains="Web-series").order_by('-Releaseyear')
        data = Serie.count()
    else:
        Serie = movies.objects.filter(session__name__icontains="Web-series")
    data = Serie.count()
    paginator = Paginator(Serie, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_pages = paginator.num_pages

    context = {

        'Serie': Serie,
        'data': data,
        'page_obj': page_obj,
        'total_pages': total_pages
    }
    return render(request, "series.html", context)


def seriesdetail(request, id):
    serie = movies.objects.get(id=id)
    data1 = media.objects.filter(movie_id=serie)
    data2 = data1.count()
    context = {
        'cat': cat,
        'serie': serie,
        'data2': data2,
        'data1': data1

    }
    return render(request, "seriessingle.html", context)


def Subscribe(request):
    if request.POST:
        email1 = request.POST['email1']
        obj = subscribe(email1=email1)
        obj.save()
        subject = "thanks you for registering to our site"
        message = 'successfully register in our website'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email1]
        send_mail(subject, message, email_from, recipient_list)
        return redirect('/')


    return render(request, "footer.html")
