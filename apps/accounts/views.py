from rest_framework import status, generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import User
from apps.accounts.serializers import CreateUserRegisterSerializer, UserLoginSerializer, UserUpdateSerializer


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
            return Response({"message": "Login successful.", "tokens": tokens}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(APIView):
    def get(self,request,pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"message":"User not found"},status=status.HTTP_404_NOT_FOUND)

        serializer = UserUpdateSerializer(user)
        return Response(serializer.data)

    def put(self,request,pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"errors":"User not found"},status=404)

        serializer = UserUpdateSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message":"User updated","user":serializer.data},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self,request,pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"errors":"User not found"},status=404)

        serializer = UserUpdateSerializer(instance=user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message":"User updated","user":serializer.data},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def delete(self,request,pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response({"message":"User successfully deleted"},status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"errors":"User not found"},status=404)


