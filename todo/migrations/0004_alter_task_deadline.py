# Generated by Django 5.0.1 on 2024-01-07 16:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0003_alter_task_options_alter_task_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
