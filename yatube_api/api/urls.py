from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'api/v1/posts', PostViewSet)
router.register(r'api/v1/groups', GroupViewSet)
router.register(r'api/v1/posts/(?P<post_id>[^/.]+)/comments', CommentViewSet,
                basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
