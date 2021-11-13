import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods
from application.settings import TEMPLATE_DIR
from .models import Users
from .forms import UserForm
from django.contrib import messages
from django.views.generic import ListView


class HomeUsers(ListView):
    model = Users
    template_name = os.path.join(TEMPLATE_DIR, 'users/home_users_list.html')
    context_object_name = 'users'
    # только для статичных данных! (для нестатичных переопределяется метод get_context_data
    extra_context = {'title': 'Service users'}
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Service users'
        return context


@login_required(login_url='/admin/')
@require_http_methods(["GET", "POST"])
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Form submission successful')
            return redirect(user)
    else:
        form = UserForm()
    return render(request, os.path.join(TEMPLATE_DIR, 'users/add_user.html'),
                  context={'title': 'Add user', 'form': form})


@require_GET
def user_detail(request, pk):
    user = get_object_or_404(Users, pk=pk)
    return render(request, os.path.join(TEMPLATE_DIR, 'users/view_user.html'),
                  context={'title': f'User {user.last_name}', 'user': user})


@require_GET
def register(request):
    return render(request, os.path.join(TEMPLATE_DIR, 'users/register_user.html'),
                  context={'title': 'Registration of new user'})


@require_GET
def login(request):
    return render(request, os.path.join(TEMPLATE_DIR, 'users/login_user.html'),
                  context={'title': 'Login user'})