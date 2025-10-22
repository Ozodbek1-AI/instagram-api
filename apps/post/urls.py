from django.urls import path

from apps.post.views import UserCreatePostAPIView, CategoryCreateAPIView

app_name = 'post'

urlpatterns = [
    path('user-create-post/',UserCreatePostAPIView.as_view(),name='user-create-post'),
    path('user-create-cat/',CategoryCreateAPIView.as_view(),name='user-create-cat'),
]