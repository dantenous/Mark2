from rest_framework import serializers

from .models import Domacnost


class Serial(serializers.ModelSerializer):

    class Meta:
        model = Domacnost
        fields = ('cas', 'teplota', 'tlak', 'vlhkost', 'teplotav', 'teplotazdanliva',
                  'rosnybod', 'vlhostv', 'densrazky', 'tlakv', 'smervetru', 'rychlostvetru', 'narazovyvitr', 'co2')
