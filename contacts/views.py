from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Contact

from .utils import Util
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class ContactCreateView(CreateView):
    model = Contact
    template_name = 'index.html'
    fields = ['name', 'email', 'subject', 'message']
    success_message = "%(name)s, sent message successfully"

    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        subject = form.instance.subject
        email = form.instance.email
        email_body = form.instance.message
        data = {
            'email_body': email_body,
            'email_subject': subject,
            'to_email': email
        }
        Util.send_email(data)
        return super().form_valid(form)
