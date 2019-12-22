from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import PasswordResetForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


class PasswordResetView(auth_views.PasswordResetView):
    form_class = PasswordResetForm
    subject_template_name = 'mails/password_reset/subject.txt'
    email_template_name = 'mails/password_reset/body.txt'
    template_name = 'password_reset.html'
    success_url = reverse_lazy('accounts:password_reset_done')


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:password_reset_complete')
    template_name = 'password_reset_confirm.html'


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'
