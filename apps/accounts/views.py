from rest_framework import status, generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import User
from apps.accounts.serializers import CreateUserRegisterSerializer, UserLoginSerializer


class UserRegisterCreateAPIView(CreateAPIView):
    serializer_class = CreateUserRegisterSerializer
    queryset = User.objects.all()


class UserLoginAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            tokens = user.get_tokens()
            return Response({"message": "Login successful", "tokens": tokens}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)