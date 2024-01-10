# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
import requests
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': serializer.data})


class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    # def patch(self, request, **kwargs):(не работает)
    #     pk = kwargs.get('pk')
    #     instance = Sensor.objects.get(id=pk)
    #     serializer = SensorSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #       serializer.save()
    #     return Response({'status': request.data})
    def patch(self, request, **kwargs):
        pk = kwargs.get('pk')
        instance = Sensor.objects.get(id=pk)
        if request.data.get('name'):
            instance.name = request.data.get('name')
        if request.data.get('description'):
            instance.description = request.data.get('description')
            instance.save()
        return Response({'status': request.data})

class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        sensor = Sensor.objects.get(id=request.data.get('sensor'))
        temperature = request.data.get('temperature')
        Measurement(sensor=sensor, temperature=temperature).save()
        return Response({'status': request.data})
