from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListAPIView.as_view()),
    path('<int:pk>/', views.ArticleDetailAPIView.as_view()),
    path('create/', views.ArticleCreateAPIView.as_view()),
    path('<int:pk>/update/', views.ArticleUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ArticleDestroyAPIView.as_view())
]