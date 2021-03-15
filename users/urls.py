from django.urls import path

from .views import home_view, signup_view, dashboard_view

app_name = "users"

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='sign-up'),
    path('signup/Client', signup_view, name='Client_sign-up'),
    path('signup/Internal', signup_view, name='Internal_sign-up'),
    path('dashboard/', dashboard_view, name='dashboard'),

]
