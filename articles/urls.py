from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
]   