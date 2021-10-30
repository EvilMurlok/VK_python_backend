import os
from django.shortcuts import render
from django.http import JsonResponse, Http404
from application.settings import TEMPLATE_DIR
from .models import Users


# render the page with te list of users
def index(request):
    ordered_users = Users.objects.order_by('-personal_acc_hcs')
    return render(request, os.path.join(TEMPLATE_DIR, 'users/index.html'),
                  {'title': 'Service users', 'users': ordered_users})


# get detailed information about the user using a GET request
def user_detail(request):
    try:
        user_id = request.GET.get('user_id')
        user = Users.objects.get(pk=user_id)
    except:
        raise Http404
    return JsonResponse({f'{user.name}': [f'{user.date_of_birth}',
                                          f'{user.personal_acc_hcs}',
                                          f'{user.personal_acc_landline_phone}',
                                          f'{user.personal_acc_distance_phone}']})



