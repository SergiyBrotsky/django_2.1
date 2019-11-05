from django.urls import path

from .views import index, by_rubruc
from .views import BbCreativeView

urlpatterns = [
    path('add/', BbCreativeView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubruc,name='by_rubric'),
    path('', index,name='index')
]