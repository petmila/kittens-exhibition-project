from rest_framework import serializers

from . import models
from .models import Kitten, Breed
from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerializer
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
#         extra_kwargs = {
#             'first_name': {'required': True},
#             'last_name': {'required': True}
#         }
#
#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})
#
#         return attrs
#
#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name']
#         )
#
#         user.set_password(validated_data['password'])
#         user.save()
#
#         return user

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']


class CurrentUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']


class KittenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitten
        # user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
        # user = serializers.CharField(source="user.username", read_only=True)
        # fields = ['id', 'name', 'age', 'color', 'breed', 'description']
        exclude = ['user']

    #     extra_kwargs = {'user': {'write_only': True}}
    #
    # def create(self, validated_data):
    #     kitten = Kitten(
    #         name=validated_data['name'],
    #         age=validated_data['age'],
    #         color=validated_data['color'],
    #         breed=validated_data['breed'],
    #         description=validated_data['description'],
    #         user=self.context.request.user
    #     )
    #     kitten.save()
    #     return kitten


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name']


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'grade_value', 'user', 'kitten']
