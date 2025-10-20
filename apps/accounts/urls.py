from django.urls import path

from apps.accounts.views import UserRegisterCreateAPIView, UserLoginAPIView

app_name = 'accounts'

urlpatterns = [
    path('create-user-register/',UserRegisterCreateAPIView.as_view(),name='create-user-register'),
    path('user-login/',UserLoginAPIView.as_view(),name='user-login'),
    # path('create-user-register/',CreateUserRegisterAPIView.as_view(),name='create-user-register'),
    # path('create-user-register/',CreateUserRegisterAPIView.as_view(),name='create-user-register'),
    # path('create-user-register/',CreateUserRegisterAPIView.as_view(),name='create-user-register'),
    # path('create-user-register/',CreateUserRegisterAPIView.as_view(),name='create-user-register'),
    # path('create-user-register/',CreateUserRegisterAPIView.as_view(),name='create-user-register'),
    # path('create-user-register/',CreateUserRegisterAPIView.as_view(),name='create-user-register'),
]