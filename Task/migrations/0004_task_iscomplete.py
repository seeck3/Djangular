# Generated by Django 2.1.5 on 2019-01-31 01:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0003_remove_task_iscomplete'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='isComplete',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
