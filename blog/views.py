from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Post, Comment, Packages
from .forms import PostForm, CommentForm, PackageForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

#def package_list(request):


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def add_package(request):
	if request.method == "POST":
		form = PackageForm(request.POST)
		if form.is_valid():
			package = form.save(commit=False)
			package.user = request.user
			package.save()
			return redirect('package_detail', pk=package.pk)
	else:
		form = PackageForm()
	return render(request, 'blog/package_edit.html', {'form': form})



# Done not so pretty...RESTful maybe??
#All packages.
@login_required
def package_list_0(request):
	packages = Packages.objects.all().order_by('deliver_till')
	time_threshold = datetime.now() + timedelta(days=5)
	results = Packages.objects.filter(deliver_till__lt=time_threshold)
	# if expression1:
	# packages = Packages.objects.filter(is_package_delivered=False).order_by('deliver_till')
	# elif expression2:
	# packages = Packages.objects.filter(is_package_delivered=True).order_by('deliver_till')
	# else:
	# packages = Packages.objects.all().order_by('deliver_till')

	return render(request, 'blog/package_list.html', {'packages': packages})
#Not delivered packages.
@login_required
def package_list_1(request):
	packages = Packages.objects.filter(is_package_delivered=False).order_by('deliver_till')
	return render(request, 'blog/package_list.html', {'packages': packages})
#Delivered packages.
@login_required
def package_list_2(request):
	packages = Packages.objects.filter(is_package_delivered=True).order_by('deliver_till')
	return render(request, 'blog/package_list.html', {'packages': packages})

@login_required
def package_detail(request, pk):
	package = get_object_or_404(Packages, pk=pk)
	return render(request, 'blog/package_detail.html', {'package': package})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
	return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('blog.views.post_detail', pk=pk)

@login_required
def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('blog.views.post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)
