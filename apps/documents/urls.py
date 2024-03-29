from django.urls import path
from .views import HomePageView,CreateDocumentView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("upload/", CreateDocumentView.as_view(), name="add_post")
]