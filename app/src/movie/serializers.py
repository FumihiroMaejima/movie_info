# from django.contrib.auth.models import Your model
from rest_framework import serializers

class InputDataValidator:
    def __call__(self, inputData):
        if inputData == '':
            raise serializers.ValidationError("your input data is wrong.")
        if inputData == None:
            raise serializers.ValidationError("your input data is wrong.")
        return inputData

class InputDataValidationSerializer(serializers.Serializer):
    inputData = serializers.CharField(validators=[InputDataValidator()])
