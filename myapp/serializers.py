from rest_framework import serializers
from .models import Student,Homework

def validate_age(age):
    if age < 18:
        return serializers.ValidationError('Too young')
    else:
        return age

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField(validators=[validate_age])
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.age = validated_data.get('age',instance.age)
        instance.updated_at = validated_data.get('updated_at',instance.updated_at)
        instance.save()
        return instance

class HomeworkSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255)
    mission = serializers.CharField(max_length=255)

    def create(self,validated_data):
        return Homework.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.subject = validated_data.get('subject',instance.subject)
        instance.mission = validated_data.get('mission',instance.mission)
        instance.save()
        return instance