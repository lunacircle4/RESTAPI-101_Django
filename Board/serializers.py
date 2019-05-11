from rest_framework import serializers
from . import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'content', 'publishedDate', 'updatedDate')
        model = models.Post
