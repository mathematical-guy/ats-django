from django_filters import rest_framework as filters
from django.contrib.postgres.search import TrigramSimilarity


class CandidateFilter(filters.FilterSet):
    name = filters.CharFilter(method='name__in', field_name='name')

    def name__in(self, queryset, field, value, **kwargs):
        qs = queryset.annotate(
            similarity=TrigramSimilarity('name', value)
        ).order_by('similarity').filter(similarity__gte=0.15)

        return qs

