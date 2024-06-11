# Generated by Django 5.0.4 on 2024-05-23 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("system", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="advanceduser",
            name="overtime_hours",
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="biographie",
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name="Biografie"
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="copyright",
            field=models.BooleanField(
                default=False, verbose_name="Zustimmung Urheberrecht"
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="disclaimer",
            field=models.BooleanField(
                default=False, verbose_name="Zustimmung Haftungsausschluss"
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="discord_username",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="Discord Benutzername",
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="epicgames_username",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="Epic Games Benutzername",
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="facebook_username",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="Facebook Benutzername",
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="instagram_username",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="Instagram Benutzername",
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="linkedin_username",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="LinkedIn Benutzername",
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="pinterest_username",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="Pinterest Benutzername",
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="playstation_username",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="PlayStation Benutzername",
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="privacy",
            field=models.BooleanField(
                default=False, verbose_name="Zustimmung Datenschutzerklärung"
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="reddit_username",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Reddit Benutzername"
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="snapchat_username",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="Snapchat Benutzername",
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="steam_username",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Steam Benutzername"
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="terms",
            field=models.BooleanField(
                default=False, verbose_name="Zustimmung Nutzungsrichtlinien"
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="threads_username",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="Threads Benutzername",
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="tiktok_username",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="TikTok Benutzername"
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="twitter_username",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="X (Twitter) Benutzername",
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="xbox_username",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Xbox Benutzername"
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="xing_username",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Xing Benutzername"
            ),
        ),
        migrations.AlterField(
            model_name="advanceduser",
            name="youtube_username",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="YouTube Benutzername",
            ),
        ),
    ]
