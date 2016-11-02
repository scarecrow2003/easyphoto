from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'^job', JobViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]