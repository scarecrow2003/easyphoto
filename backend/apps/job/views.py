from rest_framework import viewsets
from rest_framework.response import Response
from .models import EPJob
from .serializers import JobSerializer


# Create your views here.
class JobViewSet(viewsets.ModelViewSet):
    queryset = EPJob.objects.all()

    def list(self, request):
        return Response({'data': JobSerializer(Job.objects.all(), many=True).data})
