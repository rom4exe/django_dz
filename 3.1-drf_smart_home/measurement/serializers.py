from rest_framework import serializers
# TODO: опишите необходимые сериализаторы
from .models import Sensor, Measurement

class SensorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return (Sensor.objects.create(**validated_data))

    # def update(self, instance, validated_data):
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.save()
    #     return instance
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'created_at', 'sensor_id']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(source='readings', many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']