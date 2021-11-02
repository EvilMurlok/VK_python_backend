import os
from django.shortcuts import render
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from application.settings import TEMPLATE_DIR
from .models import Users


# render the page with te list of users
def index(request):
    users = Users.objects.all()
    return render(request, os.path.join(TEMPLATE_DIR, 'users/index.html'),
                  {'title': 'Service users', 'users': users})


# get detailed information about the user using a GET request
# !!!!   @api_view(['GET'])
def user_detail(request):
    if request.method != 'GET':
        return HttpResponseBadRequest('GET required')
    try:
        user_id = request.GET.get('user_id')
        user = Users.objects.get(pk=user_id)
    except Users.DoesNotExist:
        raise Http404('No News matches the given query.')
    return JsonResponse({f'{user.name}': [f'{user.date_of_birth}',
                                          f'{user.personal_acc_hcs}',
                                          f'{user.personal_acc_landline_phone}',
                                          f'{user.personal_acc_distance_phone}']})
