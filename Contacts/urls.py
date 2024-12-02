from django.urls import path
from .views import ContactListView, ContactCreateView
urlpatterns = [
    path("", ContactListView.as_view(), name="contact_list"),
    path("create/", ContactCreateView.as_view(), name="contact_create"),
]