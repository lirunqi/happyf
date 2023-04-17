from rest_framework import serializers
from .models import *


class BeforeMatchSer(serializers.ModelSerializer):
    class Meta:
        model = BeforeMatch
        fields = ['date_time',
                  'matchid',
                  'series',
                  'compid',
                  'home_odd',
                  'guest_odd',
                  'odd_term', ]

class TestFt(serializers.ModelSerializer):
    # id = serializers.IntegerField(source='pk', read_only=True)
    class Meta:
        model = Testft
        fields = "__all__"

class TestftSer(serializers.ModelSerializer):
    class Meta:
        model = Testft
        fields = "__all__"