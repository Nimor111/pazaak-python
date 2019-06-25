from django.urls import path
from .views import BoardView


urlpatterns = [
    path('', BoardView.as_view()),
]
