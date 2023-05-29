from django.urls import path
from announcements import views

urlpatterns = [
    path('announcement/', views.AnnouncementList.as_view()),
    path('announcement/admin', views.AnnouncementCreate.as_view()),
    path('announcement/admin/<int:pk>', views.AnnouncementDetail.as_view()),
]
