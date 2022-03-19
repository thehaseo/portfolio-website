from django.urls import path
from . import views

app_name = "main_page"
urlpatterns = [
    path('', views.redirect_main_english),
    path('lan=<str:language>', views.MainPageView.as_view(), name="main_page_view"),
]