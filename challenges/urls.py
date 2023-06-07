from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('<int:month>', views.my_monthly_challenge_by_number),
    path('<str:month>/', views.my_monthly_challenge, name='month-challenge'),
]
