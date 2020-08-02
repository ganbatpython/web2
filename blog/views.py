from django.shortcuts import render
from django.http import HttpResponse
from . models import Category, Post


def index(request):
    category_list = Category.objects.all().order_by('name')
    context = {
        'categories': category_list
    }
    return render(request, 'index.html', context)

def post(request, id): 
    print('category id --->', id)   
    category_list = Category.objects.all().order_by('name')
    post_list = Post.objects.filter(category__id =id)

    context = {
        'categories': category_list,
        'posts': post_list
    }
    return render(request, 'post.html', context)

