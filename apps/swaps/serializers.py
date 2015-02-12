from rest_framework import serializers
from models import *


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item


class SwapSerializer(serializers.ModelSerializer):

    class Meta:
        model = Swap


class SwapNestedSerializer(serializers.ModelSerializer):

    initiator_items = serializers.SerializerMethodField()
    other_party_items = serializers.SerializerMethodField()


    class Meta:
        model = Swap

    def get_initiator_items(self, obj):
        return ItemSerializer(obj.initiator_items.all(), many=True).data

    def get_other_party_items(self, obj):
        return ItemSerializer(obj.other_party_items.all(), many=True).data




