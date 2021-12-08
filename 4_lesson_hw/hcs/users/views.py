import os

from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods
from django.views.generic import ListView

from application.settings import TEMPLATE_DIR

from .models import Users, Receipt
from .forms import UserForm, UserRegistrationForm, UserLoginForm
from application.utils import admin_login_required, login_required


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


@admin_login_required
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


@admin_login_required
@require_http_methods(["GET", "POST"])
def delete_user(request, pk):
    user = get_object_or_404(Users, pk=pk)
    user.delete()
    messages.success(request, 'The account deleted successfully')
    return redirect('users')


@login_required
@require_GET
def show_receipts(request):
    receipts = Receipt.objects.filter(users=request.user)
    return render(request, os.path.join(TEMPLATE_DIR, 'users/available_receipts.html'),
                  context={'title': f'Receipts of {request.user.last_name} {request.user.first_name}',
                           'receipts': receipts})

@require_GET
def user_detail(request, pk):
    user = get_object_or_404(Users, pk=pk)
    return render(request, os.path.join(TEMPLATE_DIR, 'users/view_user.html'),
                  context={'title': f'User {user.last_name}', 'user_info': user})


@require_http_methods(["GET", "POST"])
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = form.save(commit=False)
            # Set the chosen password
            new_user.set_password(form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            messages.success(request, "Registration completed successfully!")
            return redirect('login')
        else:
            messages.error(request, "Registration error!")
    else:
        form = UserRegistrationForm()
    return render(request, os.path.join(TEMPLATE_DIR, 'users/register_user.html'),
                  context={'title': 'Registration of new user', 'form': form})


@require_http_methods(["GET", "POST"])
def login_user(request):
    if request.user.is_authenticated:
        messages.info(request, 'You\'ve already been authorized!')
        return redirect('news')
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Welcome back, ' + request.user.username + '!')
            return redirect('news')
        else:
            messages.error(request, 'Wrong username or email!')
    else:
        form = UserLoginForm()
    return render(request, os.path.join(TEMPLATE_DIR, 'users/login_user.html'),
                  context={'title': 'Login user', 'form': form})


@require_http_methods(["GET", "POST"])
def logout_user(request):
    logout(request)
    return redirect('login')
