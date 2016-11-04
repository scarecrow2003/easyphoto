from rest_framework import viewsets
from rest_framework.response import Response
from .models import EPJob
from ..account.models import EPAccount
from .serializers import JobSerializer
from ..account.serializers import CompanySerializer
from .managers import JobManager
from ..common.constants import ERR_CREATE_JOB


# Create your views here.
class JobViewSet(viewsets.ModelViewSet):
    queryset = EPJob.objects.all()

    def list(self, request, **kwargs):
        month = request.query_params.get('month')
        companies = EPAccount.objects.get(user=request.user).companies.all()
        jobs = EPJob.objects.filter(company_id__in=companies)
        return Response({'jobs': JobSerializer(jobs, many=True).data, 'companies': CompanySerializer(companies, many=True).data})

    def create(self, request, **kwargs):
        data = request.data
        job = JobManager.create_job(**data)
        if isinstance(job, dict) and job.get('error'):
            return Response({"result": "failed", "message": ERR_CREATE_JOB})
        return Response({'data': JobSerializer(job).data})
