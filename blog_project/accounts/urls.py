from django.urls import path
from django.views.generic import RedirectView

from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/get/', RedirectView.as_view(pattern_name='logout'), name='logout_get')
]