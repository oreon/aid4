from django.urls import path
from . import views
#from .feeds import LatestPostsFeed

app_name = 'kids'

urlpatterns = [
    # post views
   path('', views.KidListView.as_view(), name='kid_list'),
   path('mykids', views.MyKidsListView.as_view(), name='mykids_list'),
    #path('', views.PostListView.as_view(), name='post_list'),
   path('<int:pk>/', views.KidDetailView.as_view(),name='kid_detail'),
   path('sponsor/<int:kid_id>/', views.sponsor,name='sponsor'),
   path('unsponsor/<int:kid_id>/', views.unsponsor,name='unsponsor'),
   
    #path('like/', views.post_like, name='like'),
]