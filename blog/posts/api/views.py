from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import AllowAny

from blog.posts.models import Post
from blog.posts.api.serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.select_related('creator').all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
