from django.shortcuts import render
from django.views.generic import ListView
from .models import Contact
from .contact_form import ContactForm
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView
)

# Create your views here.
class ContactListView(ListView):
    model = Contact

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("contact_list")