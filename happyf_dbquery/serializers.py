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
