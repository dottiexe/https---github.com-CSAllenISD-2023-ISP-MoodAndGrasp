# Generated by Django 4.2 on 2023-04-09 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartjs', '0003_surveyquestion_delete_sliderdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyquestion',
            name='question_text',
        ),
        migrations.AddField(
            model_name='surveyquestion',
            name='question',
            field=models.TextField(default='How are you?'),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='answer',
            field=models.IntegerField(default=5),
        ),
    ]