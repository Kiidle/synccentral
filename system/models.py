from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import linebreaksbr
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


# Create your models here.
class AdvancedUser(models.Model):
    class Profile(models.TextChoices):
        NONE = "none", _("-")
        BIRD = "bird", _("Vogel")
        BUTTERFLY = "butterfly", _("Schmetterling")
        CAT = "cat", _("Katze")
        DOG = "dog", _("Hund")
        DUCK = "duck", _("Ente")
        JELLYFISH = "jellyfish", _("Qualle")
        OWL = "owl", _("Eule")
        PANDA = "panda", _("Panda")
        PENGUIN = "penguin", _("Pinguin")
        PIG = "pig", _("Schwein")
        RABBIT = "rabbit", _("Hase")
        SHEEP = "sheep", _("Schaf")
        SNAIL = "snail", _("Schnecke")
        SNAKE = "snake", _("Schlange")
        TURKEY = "turkey", _("Truthan")
        TURTLE = "turtle", _("Schildkröte")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="advanced")
    pp = models.CharField(max_length=50, choices=Profile.choices, default=Profile.NONE)

    biographie = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Biografie")
    )
    discord_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("Discord Benutzername")
    )
    epicgames_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("Epic Games Benutzername")
    )
    facebook_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("Facebook Benutzername")
    )
    instagram_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("Instagram Benutzername")
    )
    linkedin_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("LinkedIn Benutzername")
    )
    pinterest_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("Pinterest Benutzername")
    )
    playstation_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("PlayStation Benutzername")
    )
    reddit_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("Reddit Benutzername")
    )
    snapchat_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("Snapchat Benutzername")
    )
    steam_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("Steam Benutzername")
    )
    threads_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("Threads Benutzername")
    )
    tiktok_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("TikTok Benutzername")
    )
    twitter_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("X (Twitter) Benutzername")
    )
    xbox_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("Xbox Benutzername")
    )
    xing_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("Xing Benutzername")
    )
    youtube_username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("YouTube Benutzername")
    )
    privacy = models.BooleanField(
        default=False, verbose_name=_("Zustimmung Datenschutzerklärung")
    )
    terms = models.BooleanField(
        default=False, verbose_name=_("Zustimmung Nutzungsrichtlinien")
    )
    disclaimer = models.BooleanField(
        default=False, verbose_name=_("Zustimmung Haftungsausschluss")
    )
    copyright = models.BooleanField(
        default=False, verbose_name=_("Zustimmung Urheberrecht")
    )

    def format_biographie(self):
        return linebreaksbr(self.biographie)

    def format_date_joined(self):
        if self.date_joined is not None:
            formatted_date = timezone.localtime(self.date_joined).strftime(
                "%d.%m.%Y %H:%M Uhr"
            )
            return formatted_date
        else:
            return ""

    MEDIA_LOGOS = {
        "discord_username": "discord",
        "epicgames_username": "epicgames",
        "facebook_username": "facebook",
        "instagram_username": "instagram",
        "linkedin_username": "linkedin",
        "pinterest_username": "pinterest",
        "playstation_username": "playstation",
        "reddit_username": "reddit",
        "snapchat_username": "snapchat",
        "steam_username": "steam",
        "threads_username": "threads",
        "tiktok_username": "tiktok",
        "twitter_username": "x",
        "xbox_username": "xbox",
        "xing_username": "xing",
        "youtube_username": "youtube",
    }

    def format_media_usernames(self):
        media_data = []
        for field, logo in self.MEDIA_LOGOS.items():
            username = getattr(self, field, None)
            if username:
                media_data.append({"username": username, "logo": logo})
        return media_data

    def __str__(self):
        return f"{self.user.username}"


class SocialUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="social")
    friends = models.ManyToManyField(User, related_name="friends", blank=True)
    blocked = models.ManyToManyField(User, related_name="blocked_users", blank=True)

    def __str__(self):
        return f"{self.user.username}'s social network"


class InterfaceUser(models.Model):
    class Mode(models.TextChoices):
        LIGHTMODE = "light", _("Hell")
        DARKMODE = "dark", _("Dunkel")
        CONTRAST = "contrast", _("Kontrast")

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="interface"
    )
    mode = models.CharField(max_length=50, choices=Mode.choices, default=Mode.LIGHTMODE)
    gender_neutral = models.BooleanField(default=False)


class Warn(models.Model):
    class Reasons(models.TextChoices):
        ABUSE = "abuse", _("Missbrauch von Privilegien")
        ANTISEMITISM = "antisemitism", _("Antisemitismus")
        BLACKMAILING = "blackmailing", _("Erpressung")
        BULLYING = "bullying", _("Cybermobbing")
        CHILD_LIKE_IMAGERY = "child_like_imagery", _(
            "Darstellung von kinderähnlichen Merkmalen"
        )
        CHRISTOPHOBIA = "christophobia", _("Christophobie")
        COW = "cow", _("Wortwahl")
        DISCRIMINATION = "discrimination", _("Diskriminierung")
        DOXXING = "doxxing", _("Doxxing")
        EXPLOITATIVE_CONTENT = "exploitative_content", _("Ausbeuterische Inhalte")
        FACISM = "fascism", _("Faschismus")
        GROOMING = "grooming", _("Cybergrooming")
        HARASSMENT = "harassment", _("Belästigung")
        HATESPEECH = "hatespeech", _("Hassrede")
        HOMOPHOBIA = "homophobia", _("Homophobie")
        ILLEGAL_CONTENT = "illegal_content", _("Illegale Inhalte")
        ISLAMOPHOBIA = "islamophobia", _("Islamophobie")
        MISINFORMATION = "misinformation", _("Falschinformationen")
        PORNOGRAPHY = "pornography", _("Pornografie")
        PROPAGANDA = "propaganda", _("Propaganda")
        RACISM = "racism", _("Rassismus")
        RELATIVISATION = "relativisation", _("Relativierung")
        SCAM = "scam", _("Betrug")
        SEXISM = "sexism", _("Sexismus")
        SPAM = "spam", _("Spam")
        SWEARWORD = "swearword", _("Beleidigung")
        THREAT = "threat", _("Drohung")
        VIOLENT_CONTENT = "violent_content", _("Gewaltbasierter Inhalt")
        WHATABOUTISM = "whataboutism", _("Whataboutismus")
        XENOPHOBIA = "xenophobia", _("Fremdenfeindlichkeit")

    reason = models.CharField(
        max_length=50, choices=Reasons.choices, default=Reasons.ABUSE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="warns")

    def __str__(self):
        return f"{self.user.username} warned for: {self.reason}"
