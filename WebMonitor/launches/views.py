from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CommonData, LaunchData
from .serializers import LaunchDataSerializer, CommonDataSerializer


def index(request):
    try:
        launch_data = LaunchData.objects.all()
        common = CommonData.objects.all()
        return render(request, 'launches/launch.html', {'launch': launch_data, 'common': common})
    except Exception:
        return render(request, 'launches/launch-exception.html')


class CommonDataRequest(APIView):

    def get(self, request, pk=None):
        if not pk:
            queryset = CommonData.objects.all()
            serializer = CommonDataSerializer(queryset, many=True)
            return Response(serializer.data)

        queryset = CommonData.objects.get(pk=pk)
        serializer = CommonDataSerializer(queryset, many=False)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommonDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': "Method PUT not allowed"})
        try:
            instance = CommonData.objects.get(pk=pk)
        except Exception:
            return Response({'error': "Object does not exist"})

        serializer = CommonDataSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': "Method DELETE not allowed"})

        try:
            instance = CommonData.objects.get(pk=pk)
        except Exception:
            return Response({'error': "Object does not exist"})

        instance.delete()
        return Response({'info': "Object was deleted"})


class LaunchDataRequest(APIView):

    def get(self, request):
        queryset = LaunchData.objects.all()
        serializer = LaunchDataSerializer(queryset, many=True)
        return Response(serializer.data)

