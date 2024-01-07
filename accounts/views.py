from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import (
    SignUpForm
)


# Create your views here.
class SubmittableLoginView(LoginView):
    template_name = 'form.html'


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = '/viewer/authors'


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = '/viewer/movies'
