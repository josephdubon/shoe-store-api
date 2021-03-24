from django.contrib.auth.models import User, Group
from nutshell_config.nutshell_app import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url',
                  'username',
                  'email',
                  'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class NSManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.NSManufacturer
        fields = ['name', 'website']


class NSShoeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.NSShoeType
        fields = ['style', ]


class NSShoeColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.NSShoeColor
        fields = ['color_name', ]


class NSShoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.NSShoe
        fields = [
            'size',
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type',
        ]
