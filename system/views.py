from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic

from system.models import AdvancedUser, InterfaceUser, SocialUser

from .forms import BiographieForm, LoginForm, MediaForm, SignUpForm

User = get_user_model()


# Create your views here.
def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("home")
        form = LoginForm()
        return render(request, "pages/authentication/login.html", {"form": form})

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Erfolgreich angemeldet!")
                return redirect("home")

        messages.error(request, "Benutzername oder Passwort ist falsch.")
        return render(request, "pages/authentication/login.html", {"form": form})


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "pages/authentication/signup.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        AdvancedUser.objects.create(user=self.object)
        SocialUser.objects.create(user=self.object)
        InterfaceUser.objects.create(user=self.object)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def custom_logout(request):
    logout(request)
    return redirect("home")


class HomeView(generic.ListView):
    model = User
    template_name = "pages/root/home.html"


class SettingsDashboardView(generic.ListView):
    model = User
    template_name = "pages/settings/dashboard.html"


class SettingsProfileView(generic.ListView):
    model = User
    template_name = "pages/settings/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["state"] = "read"
        return context


class SettingsProfileEditBiographie(LoginRequiredMixin, generic.UpdateView):
    model = AdvancedUser
    form_class = BiographieForm
    template_name = "pages/settings/update.html"
    context_object_name = "advanced_user"

    def get_object(self, queryset=None):
        return self.request.user.advanced

    def get_success_url(self):
        return reverse_lazy("settings_profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["state"] = "update"
        context["fields"] = self.form_class().fields
        context["form_title"] = _("Biografie")
        context["form_url_name"] = "settings_profile_bio_update"
        context["form_url_pk"] = self.request.user.advanced.pk
        context["cancel_url_name"] = "settings_profile"
        return context


class SettingsMediaEditBiographie(LoginRequiredMixin, generic.UpdateView):
    model = AdvancedUser
    form_class = MediaForm
    template_name = "pages/settings/update.html"
    context_object_name = "advanced_user"

    def get_object(self, queryset=None):
        return self.request.user.advanced

    def get_success_url(self):
        return reverse_lazy("settings_profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["state"] = "update"
        context["fields"] = self.form_class().fields
        context["form_title"] = _("Medien")
        context["form_url_name"] = "settings_profile_media_update"
        context["form_url_pk"] = self.request.user.advanced.pk
        context["cancel_url_name"] = "settings_profile"
        return context


class SettingsInterfaceView(generic.ListView):
    model = User
    template_name = "pages/settings/interface.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["state"] = "read"
        return context


class SettingsFriendsView(generic.ListView):
    model = User
    template_name = "pages/settings/friends.html"


class SettingsNotificationsView(generic.ListView):
    model = User
    template_name = "pages/settings/notifications.html"


class SettingsActivitiesView(generic.ListView):
    model = User
    template_name = "pages/settings/activities.html"


class SettingsAccountView(generic.ListView):
    model = User
    template_name = "pages/settings/account.html"
