from dataclasses import fields
from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

    def validate_roll(self,value):
        if value>120:
            raise serializers.ValidationError("Out of Bound")
        return value
