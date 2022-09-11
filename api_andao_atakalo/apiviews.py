from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Exchange
from .serializers import ToySerializer, FormDataCreateToy
from .pagination import CustomPagination


class ToyList(generics.ListAPIView):
    queryset = Exchange.objects.all()
    serializer_class = ToySerializer
    pagination_class = CustomPagination


class ToyCreate(generics.CreateAPIView):
    serializer_class = FormDataCreateToy


class ExchangeView(APIView):
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FormDataCreateToy
        return ToySerializer

    def get(self, request):
        exchanges = Exchange.objects.filter(active=True).all()
        exchange_data = []
        for exchange in exchanges:
            exchange_data.append(exchange)
        return Response(exchange_data)

    def post(self, request):
        pass

    def patch(self, request, pk):
        return self.partial_update(request, )
