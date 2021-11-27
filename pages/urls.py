from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    # PostDetailView,
    # PostListView,
    # PostDetailView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('pages/about/', AboutPageView.as_view(), name='about'),
    #path('posts/', PostListView.as_view(), name='post_list'),
    #path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
