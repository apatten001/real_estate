from rest_framework import serializers
from .models import FrequentQuestionsAnswers


class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FrequentQuestionsAnswers
        fields = '__all__'

