from .models import EPJob


class JobManager(object):
    @staticmethod
    def create_job(**data):
        if 'id' in data.keys() and not data.get('id'):
            data.pop('id')
        try:

            #job = EPJob.objects.create(company=, workflow=, status=, **data)
            #return job
            return {'error': 'temp'}
        except Exception as e:
            print(e)
            return {'error': str(e)}
