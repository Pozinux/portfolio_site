from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    # A la place d'afficher tous les articles, 
    # je tri par date (le plus récent d'abord) et je veux seulement afficher les 5 derniers.
    # blogs = Blog.objects.all()
    # Finalement je le met en commentaire car sinon ça n'affiche pas le bon nombre d'articles sur la page web
    # blogs = Blog.objects.order_by('-date')[:5] 
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog_app_templates/all_blogs.html', {'blogs': blogs})
    
def detail(request, blog_id):
    # get_object_or_404 retourne un objet du blog qui correspond à l'id passé ou une page 404 s'il ne trouve pas. 
    blog = get_object_or_404(Blog, pk=blog_id)  # pk = primary key (colonne id de la base)
    return render(request, 'blog_app_templates/detail.html', {'blog': blog})