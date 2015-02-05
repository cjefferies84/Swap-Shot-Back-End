from rest_framework import serializers
from models import *


class SwapSerializer(serializers.ModelSerializer):

    class Meta:
        model = Swap


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item