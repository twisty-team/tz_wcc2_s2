from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Exchange, Owner, Picture
from .serializers import ToySerializer, FormDataCreateToy
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


class ExchangeDeactivation(APIView):
    def patch(self, request, pk):
        exchange = Exchange.objects.get(pk=pk)
        authorization = request.headers.get("Authorization")

        if authorization is None:
            return Response(
                {"message": "No authorization header provided"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token = authorization[7:]
        if len(token) == 0:
            return Response(
                {"message": "No token provided"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if token != exchange.token:
            return Response(
                {"message": "Invalid token"},
                status=status.HTTP_403_FORBIDDEN
            )

        if exchange.active == False:
            return Response(
                {"message": "This exchange is already inactive", "id": exchange.id},
                status=status.HTTP_400_BAD_REQUEST
            )

        exchange.active = False
        exchange.save()
        return Response(
            {"message": "exchange deactivated successfuly", "id": exchange.id},
            status=status.HTTP_200_OK
        )


class ExchangeView(LimitOffsetPagination, APIView):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FormDataCreateToy
        if self.request.method == 'GET':
            return ToySerializer

    def get(self, request, format=None):
        exchanges = Exchange.objects.filter(active=True).all()
        result_page = self.paginate_queryset(exchanges, request, view=self)
        exchange_serializer = ToySerializer(data=result_page, many=True)
        exchange_serializer.is_valid()
        return self.get_paginated_response(exchange_serializer.data)

    def post(self, request):
        user_name = request.data['user_name']
        contact = request.data['contact']
        owner_query_set = Owner.objects.filter(name=user_name, contact=contact)
        if len(owner_query_set) == 0:
            owner = Owner(name=user_name, contact=contact)
            owner.save()
        else:
            owner = owner_query_set[0]
        desired_toy = request.data['desired_toy']
        toy_to_change = request.data['toy_to_change']
        exchange = Exchange(toy_to_change=toy_to_change,
                            desired_toy=desired_toy, owner=owner)
        exchange.save()
        if request.FILES.getlist('pictures'):
            for files in request.FILES.getlist('pictures'):
                picture = Picture(exchange=exchange, image_url=files)
                picture.save()
        return Response({'token': exchange.token})
