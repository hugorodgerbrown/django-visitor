# Generated by Django 3.2.14 on 2022-07-26 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("visitors", "0006_alter_visitor_uuid"),
    ]

    operations = [
        migrations.AddField(
            model_name="visitor",
            name="session_expiry",
            field=models.PositiveIntegerField(
                default=0,
                help_text="Time in seconds after which visitor session should expire.",
            ),
        ),
    ]
