from django.contrib import admin
from django.urls import include, path

from system.views import (
    HomeView,
    SettingsAccountView,
    SettingsActivitiesView,
    SettingsDashboardView,
    SettingsFriendsView,
    SettingsInterfaceView,
    SettingsNotificationsView,
    SettingsProfileView,
    SignUpView,
)

from . import views

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", views.sign_in, name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", views.custom_logout, name="logout"),
    path("settings/", SettingsDashboardView.as_view(), name="settings"),
    path("settings/profile/", SettingsProfileView.as_view(), name="settings_profile"),
    path(
        "settings/interface/",
        SettingsInterfaceView.as_view(),
        name="settings_interface",
    ),
    path("settings/friends/", SettingsFriendsView.as_view(), name="settings_friends"),
    path(
        "settings/notifications/",
        SettingsNotificationsView.as_view(),
        name="settings_notifications",
    ),
    path(
        "settings/activities/",
        SettingsActivitiesView.as_view(),
        name="settings_activities",
    ),
    path(
        "settings/account/",
        SettingsAccountView.as_view(),
        name="settings_account",
    ),
]
