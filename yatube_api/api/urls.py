from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import (
    CRUDComment,
    CRUDPost,
    ListRetrieveGroup,
    RetrieveCreateFollow
)

router = SimpleRouter()

router.register('posts', CRUDPost, basename='crud_posts')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CRUDComment,
    basename='crud_comments'
)
router.register('groups', ListRetrieveGroup, basename='lr_groups')
router.register('follow', RetrieveCreateFollow, basename='rc_follow')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
