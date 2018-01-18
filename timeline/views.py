import django_filters
from django_filters import rest_framework as filters
from rest_framework import viewsets, generics
from timeline.models import HistoryTimeline, CountryModel
from timeline.serializers import TimelineSerializer, CountrySerializer
from rest_framework import permissions

# Create your views here.


class CustomFilterList(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            values = [v for v in value.split(',')]
            return qs.filter(**{'%s__%s' % (self.name, "in"): values}).distinct()
        return qs


class TimelineFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = HistoryTimeline
        fields = ['country', 'time', 'dynasty', 'person', 'address', 'abstract', 'detailed']


class CountryFilter(django_filters.rest_framework.FilterSet, django_filters.Filter):
    country = CustomFilterList(name="country")
    timeline__dynasty = CustomFilterList(name="timeline__dynasty")

    class Meta:
        model = CountryModel
        fields = ['country', 'timeline__time', 'timeline__dynasty', 'timeline__person', 'timeline__address']


class TimelineView(viewsets.ModelViewSet):
    queryset = HistoryTimeline.objects.all()
    serializer_class = TimelineSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_class = TimelineFilter


class CountryView(viewsets.ModelViewSet):
    queryset = CountryModel.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_class = CountryFilter
