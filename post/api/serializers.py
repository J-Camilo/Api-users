from rest_framework.serializers import ModelSerializer 
from post.models import Post


class PostSerializers (ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'nombre', 'email', 'edad']