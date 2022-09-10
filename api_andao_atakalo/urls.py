from django.urls import path
from .apiviews import ToyList

urlpatterns = [
    path("echange", ToyList.as_view(), name="toy_list"),
]
