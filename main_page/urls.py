from django.urls import path
from . import views

app_name = "main_page"
urlpatterns = [
    path('', views.MainPageView.as_view(), name="main_page_view"),
    path('download-cv/', views.download_cv, name='download_cv')
]