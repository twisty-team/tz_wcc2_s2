from django.urls import path
from .apiviews import ExchangeView

urlpatterns = [
    path("exchanges", ExchangeView.as_view()),
    # path("exchanges/<int:pk>", ),
]
