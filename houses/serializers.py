from rest_framework import serializers
from .models import HomeListing


class HomeListingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = HomeListing
        fields = '__all__'

