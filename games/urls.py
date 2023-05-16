from django.urls import path
from games import views

urlpatterns = [
    path('games/', views.GameList.as_view()),
    path('games/owner/', views.OwnerList.as_view()),
    path('games/owner/<int:pk>', views.OwnerEdit.as_view()),
]
