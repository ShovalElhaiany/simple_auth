from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm
from django.contrib.auth import login
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.conf import settings


class HomePageView(View):
    def get(self, request):
        return render(request=request, template_name="pages/home.html")


class UsersList(LoginRequiredMixin, ListView):
    queryset = User.objects.order_by("-date_joined")
    template_name = "pages/users_list.html"
    context_object_name = "last_users_list"
    paginate_by = settings.LIMIT


def Register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("simple_auth_app:home"))
        else:
            return redirect(reverse("register"))
    else:
        form = RegistrationForm()
        return render(
            request=request,
            template_name="registration/register.html",
            context={"form": form},
        )