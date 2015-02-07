from rest_framework import generics
from serializers import *


class SwapList(generics.ListAPIView):
    serializer_class = SwapSerializer
    queryset = Swap.objects.all()


# class SwapDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = SwapSerializer
#     queryset = Swap.objects.all()


class ItemList(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class MySwaps(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SwapSerializer
    queryset = Swap.objects.all()