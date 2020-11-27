from django.shortcuts import render
from .models import News


# Create your views here.
def main_page(request):
    news = News.objects.order_by('-created_at')
    context = {'news': news, 'title': 'Список новостей'}
    return render(request, 'index.html', context)


def about_page(request):
    return render(request, 'about.html')
