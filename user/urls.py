from django.urls import path

from user import views

urlpatterns = [
    path('signup/', views.RegisterCreateView.as_view()),
    path('login/', views.LoginView.as_view()),
]
