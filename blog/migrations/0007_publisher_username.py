# Generated by Django 5.0.3 on 2024-04-05 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_publisher_published_date_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='Username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.user'),
        ),
    ]
