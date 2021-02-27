from rest_framework import serializers
from .models import Event
from .models import Stage
class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['event_name','category','start_date','end_date','description','event_img']
class  StagesSerializer(serializers.HyperlinkedModelSerializer):
    class  Meta:
        model = Stage
        fields = ['stage_name','stage_place']
