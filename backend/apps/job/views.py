from rest_framework import viewsets
from rest_framework.response import Response
from .models import EPJob
from .serializers import JobSerializer


# Create your views here.
class JobViewSet(viewsets.ModelViewSet):
    queryset = EPJob.objects.all()

    def list(self, request, **kwargs):
        user = request.user
        return Response({'data': JobSerializer(EPJob.objects.all(), many=True).data})
