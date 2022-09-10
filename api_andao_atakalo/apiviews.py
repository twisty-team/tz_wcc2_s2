from rest_framework import generics
from .models import Toy
from .serializers import ToySerializer


class ToyList(generics.ListCreateAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
