from rest_framework import serializers
from posts.models import Post



class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=250)
    is_active = serializers.BooleanField()
    user = serializers.IntegerField(source='user_id')


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.ChoiceField(required=False, choices=Post.STATUSES)
    # category = serializers.IntegerField(source='category_id'
    category = CategorySerializer(required=True)
    user = serializers.IntegerField(required=False, source='user_id')
    title = serializers.CharField(required=True, max_length=50)
    content = serializers.CharField(required=True, max_length=250)
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.category_id = validated_data['category']['id']
        instance.content = validated_data.get('content', instance.content)
        return instance

# from posts.serializers import PostSerializer
# from posts.models import Post
# post = Post.objects.first()
# serial = PostSerializer(post, data={"title": "new title"}, partial=True)
# serial.is_valid(raise_exception=True)
# serial.save()
