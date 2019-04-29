from django.shortcuts import render,redirect, get_object_or_404
from .models import  ShortenUrl
from .auto_genarate_shoturl import auto_url
from django.utils import timezone

# Create your views here.

def home(request):
    a = ShortenUrl.objects.all()


    return render(request, 'shortener/home.html', {'a':a})

def go_to(request, url_id):

    url_to = get_object_or_404(ShortenUrl, pk=url_id)
    return redirect(url_to.url)

def create(request):

    if request.method == "POST":
        print(request.POST['urltext'])

        if request.POST['urltext'].startswith('http://') or request.POST['urltext'].startswith('https://'):
            long_url = request.POST['urltext']
        else:
            long_url = 'http://' + request.POST['urltext']


        auto_short_url = auto_url()

        shorten_url = ShortenUrl()
        shorten_url.url = long_url
        shorten_url.short_url = auto_short_url
        shorten_url.add_date = timezone.datetime.now()
        shorten_url.save()

        redirect('home')


    return render(request, 'shortener/home.html', {'short_url':shorten_url.short_url})