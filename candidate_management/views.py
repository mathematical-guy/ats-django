from rest_framework import viewsets

from candidate_management.filters import CandidateFilter
from candidate_management.models import Candidate
from candidate_management.serializers import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()
    filterset_class = CandidateFilter
