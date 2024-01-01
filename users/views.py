from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.core.mail import send_mail
from django.conf import settings
from users.models import User
from users.forms import UserRegisterForm, UserProfileForm


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset)
    #     return obj.pk

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject="Confirm registration",
            message=f'Please press this link to confirm your registration: http://127.0.0.1:8000/users/confirm/{new_user.pk}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)



class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user


def confirm_email(request, pk):
    new_person = User.objects.get(pk=pk)
    new_person.is_active = True
    new_person.save()
    return render(request, 'users/confirm_email.html', )
