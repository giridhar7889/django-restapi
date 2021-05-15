from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostList,PostDetail,PostListDetailfilter


app_name='blog_api'
#
# router=DefaultRouter()
# router.register('',PostList,basename='post')
# urlpatterns=router.urls

urlpatterns = [
    path('posts/', PostDetail.as_view(), name='detailcreate'),
    path('search/', PostListDetailfilter.as_view(), name='postsearch'),
    path('', PostList.as_view(), name='listcreate')
]