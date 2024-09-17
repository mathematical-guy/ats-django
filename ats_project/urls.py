from django.contrib import admin
from django.urls import path

from rest_framework import routers

from candidate_management.views import CandidateViewSet


router = routers.DefaultRouter()

router.register('candidates', CandidateViewSet, basename='candidates')

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls

