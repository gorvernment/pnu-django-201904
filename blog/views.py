from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post


post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            #return redirect('/blog/')
            #return redirect('blog:post_list')
            #return redirect('blog:post_detail', post.pk)
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })