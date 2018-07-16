from rest_framework import serializers, permissions, generics
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from django.contrib.auth.models import User
from cats_api.cats.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")

class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer            

class CatsSerializer(serializers.ModelSerializer):

	owner = serializers.StringRelatedField()
	class Meta:
		model = Cat
		fields = ('owner','name', 'age', 'breed', 'color', 'pk')