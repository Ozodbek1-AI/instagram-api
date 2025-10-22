from rest_framework import serializers

from apps.accounts.models import User
from apps.post.models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ["id","created_at"]

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','email','full_name','username',]
#         read_only_fields = ['id','created_at','updated_at']
#         extra_kwargs = {
#             'password': {'write_only':True}
#         }

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','descriptions','author','category','created_at']
        read_only_fields = ["id",'created_at',]
