# Generated by Django 5.0 on 2023-12-16 04:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_customuser_is_active_alter_customuser_is_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='spam_likelihood',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_phone_number',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_contact_data', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='spamreport',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
    ]
