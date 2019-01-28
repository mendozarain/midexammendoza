

from django.urls import path
from . import views

app_name = "votes"
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:candidate_id>/detail',views.detail, name='detail'),
    path('create/',views.create, name='create'),
    path('create_pos/',views.create_pos, name='create_pos'),
]
