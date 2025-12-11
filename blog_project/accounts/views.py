from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('article_list')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


class UserLoginView(LoginView):
    template_name = "accounts/login.html"