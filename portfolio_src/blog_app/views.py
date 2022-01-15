from django.shortcuts import render


def all_blogs(request):
    return render(request, 'blog_app/all_blogs.html')
