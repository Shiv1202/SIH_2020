# Generated by Django 3.0.2 on 2020-01-19 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20200120_0150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumni_user',
            old_name='email_is_active',
            new_name='is_active',
        ),
    ]