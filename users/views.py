from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the users index.")

def user_list(request):
    user_list = User.objects.order_by('last_name')
    user_dict = {'users': user_list}
    return render(request, 'users/user_list.html', context=user_dict)