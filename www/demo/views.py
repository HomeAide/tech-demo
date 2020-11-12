from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from .models import AT

# Create your views here.
def index(request):
    context = {}
    message = "Login"
    at_devices = None

    if request.user.is_authenticated:
        message = "Success"
        context['user'] = request.user
        at_devices = AT.objects.all()

    context['at_devices'] = at_devices
    context['message'] = message
    template = 'demo/index.html'

    return render(request, template, context)

def add_device(request):

    if not request.user.is_authenticated:
        # return redirect('403')
        raise PermissionDenied

    if request.method == 'POST':
        new_entry = AT(name=request.POST['name'], description=request.POST['description'], location=request.POST['location'])
        new_entry.save()
        return redirect('index')

    context = {}
    template = 'demo/add.html'

    return render(request, template, context)