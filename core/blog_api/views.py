from django.shortcuts import get_object_or_404
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, \
    IsAuthenticated
from rest_framework.response import Response


class PostUserWritePermission(BasePermission):
    message = 'Editing the post is restricted to author only '

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class PostList(viewsets.ModelViewSet):
    permission_classes =[DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

    # Define Custom Queryset
    def get_queryset(self):
        return Post.objects.all()

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
