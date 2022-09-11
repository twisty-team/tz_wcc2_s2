from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from .models import Exchange, Owner, Picture
from .serializers import ExchangeSerializer, FormDataCreateExchange


class ExchangeDeactivation(APIView):
    def patch(self, request, pk):
        exchange = Exchange.objects.get(pk=pk)
        authorization = request.headers.get("Authorization", None)

        if authorization is None:
            return Response(
                {
                    "error": "401 Unauthorized",
                    "message": "No authorization header provided"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        token = authorization[7:]
        if len(token) == 0:
            return Response(
                {
                    "error": "401 Unauthorized",
                    "message": "No token provided"
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if token != exchange.owner.token:
            return Response(
                {
                    "error": "403 Forbidden",
                    "message": "Invalid token"
                },
                status=status.HTTP_403_FORBIDDEN
            )

        if exchange.active == False:
            return Response(
                {
                    "error": "400 Bad Request",
                    "message": "This exchange is already inactive",
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        exchange.active = False
        exchange.save()
        return Response(
            {
                "message": "exchange deactivated successfuly",
                "exchange_id": exchange.id
            },
            status=status.HTTP_200_OK
        )


class ExchangeView(PageNumberPagination, APIView):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FormDataCreateExchange
        if self.request.method == 'GET':
            return ExchangeSerializer

    def get(self, request, format=None):
        exchanges = Exchange.objects.filter(active=True).all()
        result_page = self.paginate_queryset(exchanges, request, view=self)
        exchange_serializer = ExchangeSerializer(data=result_page, many=True)
        exchange_serializer.is_valid()
        return self.get_paginated_response(exchange_serializer.data)

    def post(self, request):
        def check_phone_number_format(phone_number):
            if len(phone_number) != 10:
                return False
            for i in phone_number:
                if i not in "0123456789":
                    return False
            return True
            
        data = {}

        try:
            user_name = request.data['user_name']
            contact = request.data['contact']
            desired_toy = request.data['desired_toy']
            toy_to_change = request.data['toy_to_change']
        except:
            return Response(
                {
                    "error": "400 Bad Request",
                    "message": "One or more of the following field is missing : (user_name, contact, desired_toy, toy_to_change)."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        for i in [user_name, contact, desired_toy, toy_to_change]:
            if len(i) == 0:
                return Response(
                    {
                        "error": "400 Bad Request",
                        "message": "None of the field can be empty"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        if not check_phone_number_format(contact):
            return Response(
                {
                    "error": "400 Bad Request",
                    "message": "Invalid phone number format"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        owner_query_set = Owner.objects.filter(name=user_name, contact=contact)
        if len(owner_query_set) == 0:
            try:
                owner = Owner(name=user_name, contact=contact)
                owner.save()
            except:
                return Response(
                    {
                        "error": 400,
                        "message": "(user_name, contact) must be unique."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            data["token"] = owner.token
            data["message"] = "Store this token somewhere secure as you will need to provide it in an Authorization header in order to deactivate an exchange."
        else:
            owner = owner_query_set[0]

        exchange = Exchange(toy_to_change=toy_to_change,
                            desired_toy=desired_toy, owner=owner)

        exchange.save()

        data["exchange_id"] = exchange.id

        if request.FILES.getlist('pictures'):
            for files in request.FILES.getlist('pictures'):
                picture = Picture(exchange=exchange, image_url=files)
                picture.save()

        data["success"] = True

        return Response(data, status=status.HTTP_201_CREATED)
