# TODO: опишите сериализаторы
from rest_framework import serializers
from measurements.models import Project, Measurement

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name', 'latitude', 'longitude']


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['value', 'project', 'image']