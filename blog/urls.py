from django.urls import path
from . import views
from profile import views as userViews

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)





app_name = 'blog'

urlpatterns = [
    path('posts/', views.PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='home'),
    # path('posts/', views.PostViewSet.as_view({'get': 'list'}), name='posts'),
    path('posts/<slug>/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve'})),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get-csrf-token/', userViews.get_csrf_token, name='csrf-token'),
    path('user/register/', userViews.UserCreateView.as_view(), name='register'),
    path('api/create_article/', views.create_posts, name='create_posts'),
    path('create/', views.post_blog, name='create'),
    path('', views.post_list, name="home"),
    path('<slug>-<int:pk>/', views.post_detail, name='post_detail'),
    # path('<slug>-<int:pk>/update', views.PostUpdateView.as_view, name='post_update'),
    path('<slug>-<int:pk>/update', views.post_update, name='post-update'),
    path('<slug>-<int:pk>/delete', views.post_delete, name='post-delete'),
]