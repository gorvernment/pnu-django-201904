import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment
from .forms import CommentForm, PostForm

# Create your views here.
def post_list(request):
    return render(request, 'travel/post_list.html', {
        'post_list': Post.objects.all(),
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'travel/post_detail.html', {
        'post': post,
        'comment_form': CommentForm(),
    })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            #return redirect(post)  #Post 모델에 get_absolute_url 구현되어 있어야 사용 가능
            return redirect('/travel/{}/'.format(post.pk))  #url reverse 기능 이용
    else:
        form = PostForm()
    return render(request, 'travel/post_form.html', {
        'form' : form,
    })

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('/travel/{}/'.format(post.pk))
    else:
        form = PostForm(instance=post)
    return render(request, 'travel/post_form.html', {
        'form' : form,
    })

def comment_list(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    qs = Comment.objects.all().filter(post__pk=post_pk)
   
    # message, author, created_at, pk
    obj_list = [{  # List Comprehension
        'pk': comment.pk,
        'message': comment.message,
        'author': str(comment.author),
        'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S'),
    } for comment in qs]

    # json_string = json.dumps(obj_list, ensure_ascii=False)
    # return HttpResponse(json_string)

    return JsonResponse(obj_list, safe=False)

    # return render(request, 'travel/comment_list.html', {
    #     'post': post,
    #     'comment_list': qs,
    # })
    

@login_required
def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    # comment_list = post.comment_set.all()
    # # comment_list = Comment.objects.filter(post=post)
    # comment_list = comment_list.order_by('-id')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            #return redirect('travel:post_detail', post_pk)
            return redirect(post)
    else:
        form = CommentForm()
    return render(request, 'travel/comment_form.html', {'form': form})

@login_required
def comment_edit(request, post_pk, pk):
    comment = get_object_or_404(Comment, author=request.user, pk=pk)
    # if comment.author != request.user:

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            #return redirect('travel:post_detail', post_pk)
            return redirect(comment.post)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'travel/comment_form.html', {'form': form})

@login_required
def comment_delete(request, post_pk, pk):
    comment = get_object_or_404(Comment, author=request.user, pk=pk)
    if request.method == 'POST':
        comment.delete()  # 호출 즉시 DELETE 쿼리 수행
        #return redirect('travel:post_detail', post_pk)
        return redirect(comment.post)
    return render(request, 'travel/post_confirm_delete.html', {
        'comment': comment,
    })