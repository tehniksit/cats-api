from rest_framework import serializers

from cats_api.cats.models import Cat, User

class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name' )

class CatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = ('name', 'age', 'breed', 'color')