import re

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxLengthValidator
from django.forms import ModelForm

from system.models import AdvancedUser

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(ModelForm):
    first_name = forms.CharField(validators=[MaxLengthValidator(50)])
    last_name = forms.CharField(validators=[MaxLengthValidator(50)])
    username = forms.CharField(validators=[MaxLengthValidator(50)])
    email = forms.EmailField(validators=[MaxLengthValidator(50)])
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        help_texts = {"username": ""}
        error_messages = {"name": {"required": "Pflichtfeld"}}

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("Username ist ein Pflichtfeld")
        if " " in username:
            raise forms.ValidationError(
                "Benutzername ist nur diese Format ist erlaubt 'vorname_nachname'. Daten von Majestic!"
            )
        if not re.match("^[a-z0-9_.]+$", username):
            raise forms.ValidationError(
                "Benutzername ist nur diese Format ist erlaubt 'vorname_nachname'. Daten von Majestic!"
            )
        return username.lower()

    def save(self, commit=True):
        user = super().save(commit=commit)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class BiographieForm(forms.ModelForm):
    class Meta:
        model = AdvancedUser
        fields = ["biographie"]


class MediaForm(forms.ModelForm):
    class Meta:
        model = AdvancedUser
        fields = [
            "discord_username",
            "epicgames_username",
            "facebook_username",
            "instagram_username",
            "linkedin_username",
            "pinterest_username",
            "playstation_username",
            "reddit_username",
            "snapchat_username",
            "steam_username",
            "threads_username",
            "tiktok_username",
            "twitter_username",
            "xbox_username",
            "xing_username",
            "youtube_username",
        ]
