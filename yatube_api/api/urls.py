from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import CommentViewSet, FollowsViewSet, GroupViewSet, PostViewSet


app_name = 'api'

v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
v1_router.register('follow', FollowsViewSet, basename='follows')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(v1_router.urls)),
]
