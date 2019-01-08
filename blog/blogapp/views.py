from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, UserRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        form  = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/ ')
    else:
        form = UserRegisterForm()
    return render(request,'blogapp/register.html',{'form':form})





def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request,'blogapp/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request , 'blogapp/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blogapp/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return redirect(request, 'blog/post_edit.html', {'form': form})