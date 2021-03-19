from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loans', views.calculate_interest, name='index'),
    # path('', include('loanapp.urls')),
]
