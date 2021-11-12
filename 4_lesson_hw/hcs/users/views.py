import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404
from django.views.decorators.http import require_GET, require_http_methods
from application.settings import TEMPLATE_DIR
from .models import Users
from .forms import UserForm
from django.views.generic import ListView


class HomeUsers(ListView):
    model = Users
    template_name = os.path.join(TEMPLATE_DIR, 'users/home_users_list.html')
    context_object_name = 'users'
    # только для статичных данных! (для нестатичных переопределяется метод get_context_data
    extra_context = {'title': 'Service users'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Service users'
        return context


@require_http_methods(["GET", "POST"])
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(user)
    else:
        form = UserForm()
    return render(request, os.path.join(TEMPLATE_DIR, 'users/add_user.html'),
                  context={'title': 'Add user', 'form': form})


@require_GET
def user_detail(request, pk):
    user = get_object_or_404(Users, pk=pk)
    return render(request, os.path.join(TEMPLATE_DIR, 'users/view_user.html'),
                  context={'title': f'User {user.name}', 'user': user})
    # return JsonResponse({f'{user.name}': [f'{user.date_of_birth}',
    #                                       f'{user.personal_acc_hcs}',
    #                                       f'{user.personal_acc_landline_phone}',
    #                                      f'{user.personal_acc_distance_phone}']})
