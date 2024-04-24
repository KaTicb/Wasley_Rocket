from rest_framework import serializers
from .models import LaunchData, CommonData


class LaunchDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaunchData
        fields = '__all__'


class CommonDataSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    whose_param = serializers.CharField(max_length=20, default="Atmosphere")
    measure = serializers.CharField(max_length=20)
    value = serializers.FloatField()
    measure_time = serializers.DateTimeField()
    dimension = serializers.CharField(max_length=5)
    launch_id = serializers.PrimaryKeyRelatedField(queryset=LaunchData.objects.all())

    def create(self, validated_data):
        return CommonData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.whose_param = validated_data.get('whose_param', instance.whose_param)
        instance.measure = validated_data.get('measure', instance.measure)
        instance.value = validated_data.get('value', instance.value)
        instance.measure_time = validated_data.get('measure_time', instance.measure_time)
        instance.dimension = validated_data.get('dimension', instance.dimension)
        instance.launch_id = validated_data.get('launch_id', instance.launch_id)
        instance.save()
        return instance
