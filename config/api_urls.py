from rest_framework.routers import DefaultRouter

from blog.posts.api.views import PostViewSet


router = DefaultRouter()

router.register('posts', PostViewSet, 'post')

urlpatterns = router.urls