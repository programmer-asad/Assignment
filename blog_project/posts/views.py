from django.shortcuts import render, redirect
from .import forms
from .import models
from django.db.models import Q

def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})


def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    
    return redirect ('homepage')



def search_posts(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        # Filtering posts by category or title based on the search query
        results = models.Post.objects.filter(
            Q(category__icontains=query) | Q(title__icontains=query)
        )

    return render(request, 'search_results.html', {'results': results, 'query': query})