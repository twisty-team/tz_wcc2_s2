from rest_framework import generics
from .models import Toy
from .serializers import ToySerializer, FormDataCreateToy
from .pagination import CustomPagination


class ToyList(generics.ListAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
    pagination_class = CustomPagination


class ToyCreate(generics.CreateAPIView):
    serializer_class = FormDataCreateToy
