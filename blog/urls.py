from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostsView.as_view(), name='home'),
    # path('', views.post_list, name='home'),
   

    path('create/', views.post_blog, name='post'),
    path('<slug>-<int:pk>/', views.post_detail, name='post_detail'),
    # path('<slug>-<int:pk>/update', views.PostUpdateView.as_view, name='post_update'),
    path('<slug>-<int:pk>/update', views.post_update, name='post-update'),
    path('<slug>-<int:pk>/delete', views.post_delete, name='post-delete'),
]