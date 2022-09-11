from rest_framework.views import APIView
from .models import Toy, Owner, Picture
from .serializers import ToySerializer, FormDataCreateToy
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


class ToyList(APIView, LimitOffsetPagination):
    serializer_class = ToySerializer

    def get(self, request, format=None):
        toys = Toy.objects.all()
        result_page = self.paginate_queryset(toys, request, view=self)
        toy_serializer = ToySerializer(data=result_page, many=True)
        toy_serializer.is_valid()
        return self.get_paginated_response(toy_serializer.data)


class ToyCreate(APIView):
    serializer_class = FormDataCreateToy

    def post(self, request):
        user_name = request.data['user_name']
        contact = request.data['contact']
        owner_query_set = Owner.objects.filter(name=user_name, contact=contact)
        if len(owner_query_set) == 0:
            owner = Owner(name=user_name, contact=contact)
            owner.save()
        else:
            owner = owner_query_set[0]
        toy_name = request.data['toy_name']
        toy_to_change = request.data['toy_to_change']
        toy = Toy(name=toy_name, toy_to_change=toy_to_change, owner=owner)
        toy.save()
        if request.FILES.getlist('pictures'):
            for files in request.FILES.getlist('pictures'):
                picture = Picture(toy=toy, image_url=files)
                picture.save()
        toy_serializer = ToySerializer(data=toy, many=False)
        toy_serializer.is_valid()
        print(toy_serializer.initial_data)
        return Response(toy_serializer.data)
