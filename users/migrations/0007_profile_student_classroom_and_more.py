# Generated by Django 4.1.7 on 2023-03-28 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0006_profile_user_class_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='student_classroom',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_class', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_class_code',
            field=models.TextField(default=''),
        ),
    ]
