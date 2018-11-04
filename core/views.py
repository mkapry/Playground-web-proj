from django.shortcuts import HttpResponse

# Create your views here.
# def frount(request):
#   return HttpResponse('Hello')
from core.models import User
from django.views.generic import ListView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CreateUser(CreateView):
    template_name = "core/signup.html"
    model = get_user_model()


class UserPage(ListView):
    template_name = "core/base.html"
    model = User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/welcome/')


def logout_view(request):
    logout(request)
    return redirect('%s?next=%s' % (settings.LOGOUT_REDIRECT_URL, request.template_name))




def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/welcome/')
    else:
        form = RegistrationForm()

    return render(request, 'core/signup.html', {'form': form})
