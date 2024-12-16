from django.urls import path
from . import views
from profile import views as userViews

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



app_name = 'blog'

urlpatterns = [
    # REST API FRAMEWORK -- REACT
    path('auth/posts/', views.PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='home'),
    path('auth/posts/<slug>/<int:pk>', views.PostDetail.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get-csrf-token/', userViews.get_csrf_token, name='csrf-token'),
    path('user/register/', userViews.UserCreateView.as_view(), name='register'),
    path('api/create_article/', views.create_posts, name='create_posts'),

    # Django Web frontend development
    path('create/', views.post_blog, name='create'),
    path('', views.post_list, name="home"),
    path('<slug>-<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<slug>/<int:pk>/update', views.post_update, name='post-update'),
    path('post/<slug>/<int:pk>/delete', views.post_delete, name='post-delete')
]




# path('posts/', views.PostViewSet.as_view({'get': 'list'}), name='posts'),
# path('post/<slug>/<int:pk>/delete', views.post_delete, name='post-delete'),
# path('au/posts/<slug>/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve'})),
