from django.shortcuts import render


def all_blogs(request):
    return render(request, 'blog_app_templates/all_blogs.html')
