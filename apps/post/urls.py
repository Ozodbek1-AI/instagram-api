from django.urls import path

from apps.post.views import UserCreatePostAPIView

app_name = 'post'

urlpatterns = [
    path('user-create-post/',UserCreatePostAPIView.as_view(),name='user-create-post')
]