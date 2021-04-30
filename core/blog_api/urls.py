from django.urls import path
from .views import PostList,PostDetail

app_name='blog_api'

urlpatterns =[
    path('<int:pk>',PostDetail,name='detailcreate'),
    path('',PostList,name='listcreate')
]