from django.urls import path
from .apiviews import ExchangeView, ExchangeDeactivation

urlpatterns = [
    path("exchanges", ExchangeView.as_view()),
    path("exchanges/<int:pk>", ExchangeDeactivation.as_view()),
]
