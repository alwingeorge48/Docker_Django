from django.urls import path

from .views import Blog, Entery

app_name = 'dataview'

urlpatterns = [
    path('', dataview_view, name='dataview'),
    path('Blog/', signup_view, name='Blog'),
    path('Entry/', dashboard_view, name='Entery'),
]

