from django.urls import re_path

from . import views

app_name = 'form'
urlpatterns = [
    re_path(r'^$', views.feedback_form, name='home'),
]
