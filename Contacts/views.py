from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Contact
from .contact_form import ContactForm
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, UpdateView, DeleteView

# Create your views here.
class ContactListView(ListView):
    model = Contact

class ContactCreateView(View):
    template_name = 'contacts/contact_form.html'
    def get(self, request):
        form = ContactForm()
        context = {
            'form': form,
            'is_creation': True  
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # This will create a new Contact instance
            return redirect('contact_list')  # Redirect to the contact list page or any other page
        else:
            
            context = {
                'form': form,
                'is_creation': True
            }
        return render(request, self.template_name, context)
    
class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/contact_form.html'  # Use the same form template for update
    success_url = reverse_lazy("contact_list")
class ContactDetailView(DetailView):
    model = Contact

class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("contact_list")
    template_name = 'contacts/contact_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass an additional variable to the template
        context['is_creation'] = False  # Set it to True for update, False for create
        return context
    
class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contact_list")