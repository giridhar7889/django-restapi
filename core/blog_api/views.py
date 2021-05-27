from django.shortcuts import get_object_or_404
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, \
    IsAuthenticated,AllowAny

from rest_framework.response import Response
from rest_framework import filters


class PostUserWritePermission(BasePermission):
    message = 'Editing the post is restricted to author only '

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class PostList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.all()


class PostDetail(generics.ListAPIView):

    serializer_class = PostSerializer
    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        return Post.objects.filter(slug=slug)

class PostListDetailfilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [filters.SearchFilter]
    search_fields=['^slug']













# class PostList(viewsets.ModelViewSet):
#     permission_classes =[DjangoModelPermissionsOrAnonReadOnly]
#     serializer_class = PostSerializer
#
#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)
#
#     # Define Custom Queryset
#     def get_queryset(self):
#         user = self.request.user
#         return Post.objects.filter(author=user)
#
#
# class PostList(viewsets.ViewSet):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     queryset = Post.postobjects.all()
#
#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset,many=True)
#         return Response(serializer_class.data)
#
#     def retrieve(self, request,pk):
#         post=get_object_or_404(self.queryset,pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)
#
#

# class PostList(generics.ListCreateAPIView):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer
#     pass
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     pass
