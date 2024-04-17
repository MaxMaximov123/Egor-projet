from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from  .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

def index(request):
    arts_list = Art.objects.all()
    return render(request, 'DigitalHermitag/index.html', {'arts_list': arts_list})

def add_art(request):
    error = ''
    if request.method == 'POST':
        form = Art_form(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                f = form.save(commit=False)
                f.author = request.user
                f.save()
            else:
                form.save()
            return redirect('index')
        else:
            error = 'Неверный формат данных'

    form = Art_form()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'DigitalHermitag/add_art.html', data)


def search_page(request):
    arts_list = Art.objects.all()
    title = request.GET.get('title')
    genre = request.GET.get('genre')
    author = request.GET.get('author')
    if title != '':
        arts_list = arts_list.filter(title__iregex=title)
    if genre != '':
        arts_list = arts_list.filter(genre__iregex=genre)
    if author != '':
        arts_list = arts_list.filter(author__icontains=author)
    return render(request, 'DigitalHermitag/search_page.html', {'arts_list': arts_list, 'title': title, 'genre': genre, 'author': author})


def my_arts(request):
    arts_list = Art.objects.all()
    if request.user.is_authenticated:
        arts_list = arts_list.filter(author__icontains=request.user)
    return render(request, 'DigitalHermitag/my_arts.html', {'arts_list': arts_list})


def login(request):
    return render(request, 'DigitalHermitag/login.html')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'DigitalHermitag/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'DigitalHermitag/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')
