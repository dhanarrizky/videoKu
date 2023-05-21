from django.urls import path
from . import views as _

urlpatterns = [
    path('', _.index, name='home'),
    #path('result/<str:s>',_.search, name='search'),
]
