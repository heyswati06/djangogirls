from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import SalePost
from .forms import PostForm

# Create your views here.
def salepost_list(request):
    posts = SalePost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts = SalePost.objects.all()
    return render(request, 'bicycles/salepost_list.html', {'posts':posts})

def salepost_detail(request, pk):
    post = get_object_or_404(SalePost, pk=pk)
    return render(request, 'bicycles/salepost_detail.html', {'post': post})

def salepost_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('salepost_detail', pk=post.pk)
    form = PostForm()
    return render(request, 'bicycles/salepost_edit.html', {'form': form})

def salepost_edit(request, pk):
    post = get_object_or_404(SalePost, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('salepost_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'bicycles/salepost_edit.html', {'form': form})

