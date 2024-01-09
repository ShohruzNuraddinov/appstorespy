from django.urls import path

from app import views


urlpatterns = [
    path('create/image/', views.ImageResizeCreateView.as_view())
]
