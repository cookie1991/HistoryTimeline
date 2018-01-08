from rest_framework import serializers
from timeline.models import HistoryTimeline, CountryModel,ContinentModel


class TimelineSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = HistoryTimeline
        fields = ('time', 'dynasty', 'person', 'address', 'abstract', 'detailed')


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    # timeline = TimelineSerializer(many=True, read_only=True)

    historyTimeline = serializers.SerializerMethodField('get_timeline')

    def get_timeline(self, obj):
        # time = self.context['request'].query_params.get('timeline__time')
        dynasty = self.context['request'].query_params.get('timeline__dynasty')
        person = self.context['request'].query_params.get('timeline__person')
        address = self.context['request'].query_params.get('timeline__address')

        kwargs = {
            # 动态查询的字段
        }
        if dynasty is not None:
            kwargs['dynasty'] = dynasty
        if person is not None:
            kwargs['person'] = person
        if address is not None:
            kwargs['address'] = address

        if dynasty is None and person is None and address is None:
            htl = HistoryTimeline.objects.filter(country=obj)
        else:
            htl = HistoryTimeline.objects.filter(country=obj, **kwargs)

        serializer = TimelineSerializer(htl, many=True, read_only=True)
        return serializer.data

    class Meta:
        model = CountryModel
        fields = ('country', 'historyTimeline')
