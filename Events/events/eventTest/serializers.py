from rest_framework import serializers

class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['event_name','category','start_date','end_date','description','event_img']
