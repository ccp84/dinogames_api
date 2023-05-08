from django.urls import path
from users import views

urlpatterns = [
    path('user/<int:pk>', views.UserDetail.as_view()),
]
