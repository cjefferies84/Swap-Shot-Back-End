from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib import auth
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from django.core.context_processors import csrf
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

from serializers import *
from rest_framework.authtoken.views import ObtainAuthToken

def obtain_user_from_token(request):
    auth = TokenAuthentication()
    response = auth.authenticate_credentials(request.DATA['token'])

    user_id = response[0].id

    return HttpResponse(user_id)



# def logout(request):
#     auth.logout(request)
#     return JSONResponse([{'success': 'Logged out!'}])


# class JSONResponse(HttpResponse):
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#

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


class UserList(generics.ListCreateAPIView):
    """List all users or create a new User"""
   # permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()




class UserDetail(generics.RetrieveAPIView):
    """Retrieve, update or delete a User instance."""
    permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer