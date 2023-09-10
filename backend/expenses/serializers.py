from rest_framework import serializers
from .models import Expense

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'