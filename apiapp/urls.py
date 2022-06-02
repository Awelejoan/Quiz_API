from django.urls import path
from . import views

app_name = 'apiapp'

urlpatterns = [
    path('question', views.Firstview.as_view(),name='question'),
    path('option', views.Secondview.as_view(),name='option'),
    path('answer', views.Thirdview.as_view(),name='answer')
]