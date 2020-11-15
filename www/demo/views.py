from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import AT

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('signin')

    context = {}

    context['user'] = request.user
    at_devices = AT.objects.all()
    context['at_devices'] = at_devices

    template = 'demo/index.html'

    return render(request, template, context)

def add_device(request):
    if not request.user.is_authenticated:
        return redirect('signin')

    if request.method == 'POST':
        new_entry = AT(name=request.POST['name'], description=request.POST['description'], location=request.POST['location'])
        new_entry.save()
        return redirect('index')

    context = {}
    template = 'demo/add.html'

    return render(request, template, context)

def create_user(request):
    if not request.user.is_authenticated:
        return redirect('signin')

    new_user = ""
    password = ""

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(username=username, password=password)
            # login(request, user)
            new_user = form.cleaned_data['username']
            password = form.cleaned_data['password1']
    else:
        form = UserCreationForm()

    context = {'form': form, 'new_user': new_user, 'password': password}
    template = 'demo/create_user.html'

    return render(request, template, context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

    form = AuthenticationForm()
    return render(request, 'demo/login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')