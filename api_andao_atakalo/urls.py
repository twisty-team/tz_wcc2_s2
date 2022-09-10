from django.urls import path
from .apiviews import ToyList, ToyCreate

urlpatterns = [
    path("echange", ToyList.as_view(), name="toy_list"),
    path("create_echange", ToyCreate.as_view(), name="toy_create")
]
