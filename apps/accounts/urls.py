from django.urls import path

from apps.accounts.views import CreateUserRegisterAPIView

app_name = 'accounts'

urlpatterns = [
    path('create-user-register/',CreateUserRegisterAPIView.as_view(),name='create-user-register'),
    # path('create-user-register/',CreateUserRegisterAPIView.as_view(),name='create-user-register'),
    # path('create-user-register/',CreateUserRegisterAPIView.as_view(),name='create-user-register'),
    # path('create-user-register/',CreateUserRegisterAPIView.as_view(),name='create-user-register'),
    # path('create-user-register/',CreateUserRegisterAPIView.as_view(),name='create-user-register'),
    # path('create-user-register/',CreateUserRegisterAPIView.as_view(),name='create-user-register'),
    # path('create-user-register/',CreateUserRegisterAPIView.as_view(),name='create-user-register'),
    # path('create-user-register/',CreateUserRegisterAPIView.as_view(),name='create-user-register'),
]