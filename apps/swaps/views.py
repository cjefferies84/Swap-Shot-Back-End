from rest_framework import generics
from serializers import *
from django.http.response import HttpResponse


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

    def update(self, request, pk=None):
        obj = request.DATA
        old_swap = Swap.objects.get(id=obj['id'])
        if not (old_swap.status == obj['status']):
            if old_swap.status == 'AVAILABLE' and obj['status'] == 'PENDING':
                for i in old_swap.items:
                    i.status = 'PENDING'
                    i.save()
                old_swap.status = obj['status']
                old_swap.status.save()

            elif old_swap.status == 'PENDING' and obj['status'] == 'CLOSED':
                for i in old_swap.items:
                    i.status = 'CLOSED'
                    i.save()
                old_swap.status = obj['status']
                old_swap.status.save()
            else:
                for i in old_swap.items:
                    i.status = 'AVAILABLE'
                    i.save()
                old_swap.status = obj['status']
                old_swap.status.save()
        return HttpResponse(old_swap.status)
