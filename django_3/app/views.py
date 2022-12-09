from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
# from .forms import EmployeeForm
from .models import Posts
from .forms import PostForm, NewUserForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import numpy as np
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as dj_login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect


def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            try:
                form.save()
                post = Posts.objects.all().order_by()
                print(type(post))
                x = list(post)[-1]
                x = x.id
                return redirect(f'/new_post_details/{x}')
            except Exception as e:
                print(e)
                pass
        else:
            print("invalid")
    else:
        form = PostForm()
    instance = form.save(commit=False)
    instance.author = request.user.username
    print(instance.author)
    author = instance.author
    context = {
        'form': form,
        'author': author
    }
    return render(request, 'new_post.html', context)


def new_post_details(request, id):
    post = Posts.objects.get(pk=id)
    return render(request, 'new_post_details.html', {'post': post})


def show_post(request, id=None):
    posts = Posts.objects.all()
    page_size = 2
    index = 1
    if id is not None:
        post1 = Posts.objects.get(pk=id)
        for i in range(len(posts)):
            if post1 == posts[i]:
                print(i)
                index = i
        index = int(np.ceil((index + 1) / page_size))
        print(index)

    p = Paginator(posts, page_size)  # creating a paginator object
    # getting the desired page number from url
    page_no = index
    page_number = request.GET.get('page', page_no)
    # page_number = '2'
    print(page_number, type(page_number))
    try:
        page_obj = p.page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(p.num_pages)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
        print(page_obj)
    context = {'page_obj': page_obj}
    # print('fghj', p.num_pages, p.count)
    # sending the page object to index.html
    return render(request, 'index.html', context)
    # return render(request, "post_list.html", {'posts': posts})


def edit_post(request, id):
    post = Posts.objects.get(id=id)
    return render(request, 'edit_post.html', {'post': post})


def update_post(request, id):
    post = Posts.objects.get(id=id)
    print(post.blog_by_author)
    form = PostForm(request.POST, instance=post)
    for field in form:
        print("Field Error:", field.name, field.errors)
    print(form.is_valid())
    if form.is_valid():
        form.save()
        return redirect(f"/show_post/{id}")
    print('render')
    return render(request, 'index.html', {'post': post})


def destroy_post(request, id):
    post = Posts.objects.get(id=id)
    print(post)
    x = post.id
    print(x)
    post.delete()
    return redirect(f"/show_post/{x + 1}")


def blog_by_author(request, author):
    post = Posts.objects.filter(blog_by_author=author)
    context = {
        'posts': post,
        'author': author
    }
    return render(request, 'blog_by_author.html', context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            dj_login(request, user)
            messages.success(request, "Registration successful")
            return redirect("/show_post")
        messages.error(request, "Unsuccessful registration")
    form = NewUserForm()
    print(form)
    return render(request, 'register.html', {'register_form': form})


@csrf_protect
def login_request(request):
    print('hello')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            if user is not None:
                dj_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/show_post")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", {'login_form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/show_post")
