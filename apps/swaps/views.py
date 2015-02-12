from rest_framework import generics
from serializers import *


class SwapList(generics.ListCreateAPIView):
    serializer_class = SwapSerializer
    queryset = Swap.objects.all()

class SwapNestedList(generics.ListCreateAPIView):
    serializer_class = SwapNestedSerializer
    queryset = Swap.objects.all()


# class SwapDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = SwapSerializer
#     queryset = Swap.objects.all()


class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class SwapDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SwapSerializer
    queryset = Swap.objects.all()