# Generated by Django 5.0 on 2023-12-10 07:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Task", "0002_alter_task_t_desc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="T_desc",
            field=models.TextField(default="TASK IS ADDED ON 2023-12-10"),
        ),
    ]
