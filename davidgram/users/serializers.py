from rest_framework import serializers
from . import models
from davidgram.images import serializers as images_serializers

class UserProfileSerializer(serializers.ModelSerializer):

  # ReadOnlyField에 해당하는 것들은 수정이 불가능하다.
  images = images_serializers.CountImageSerializer(many=True, read_only=True)
  post_count = serializers.ReadOnlyField()
  followers_count = serializers.ReadOnlyField()
  following_count = serializers.ReadOnlyField()

  class Meta:
    model = models.User
    fields = (
      'profile_image',
      'username',
      'name',
      'bio',
      'website',
      'post_count',
      'followers_count',
      'following_count',
      'images',
    )


class ListUserSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.User
    fields = (
      'id',
      'profile_image',
      'username',
      'name',
    )
