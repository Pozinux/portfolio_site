from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    # A la place d'afficher tous les articles, 
    # je tri par date (le plus récent d'abord) et je veux seulement afficher les 5 derniers.
    #blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-date')[:5] 
    return render(request, 'blog_app_templates/all_blogs.html', {'blogs': blogs})
    
